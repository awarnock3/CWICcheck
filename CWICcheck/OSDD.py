import sys, getopt
import requests
from CwicCheckUtils import *
from UrlUtils import *
from ValidOsddTests import *

valid_osdds = {'Valid'      : "http://cwic.wgiss.ceos.org/opensearch/datasets/Landsat_8/osdd.xml?clientId=CWICcheck",
               'NoDatasetId': "http://cwic.wgiss.ceos.org/opensearch/datasets/osdd.xml?clientId=CWICcheck",
         }

invalid_osdds = {'BadDataset'  : "http://cwic.wgiss.ceos.org/opensearch/datasets/foobar/osdd.xml",
                 'NoClientId'  : "http://cwic.wgiss.ceos.org/opensearch/datasets/Landsat_8/osdd.xml",
                 'NoParameters': "http://cwic.wgiss.ceos.org/opensearch/datasets/osdd.xml",
         }

other_osdds = {'GCMD'      : "http://gcmddemo.gsfc.nasa.gov/KeywordSearch/default/openSearch.jsp?portal=CWIC&clientId=CWICcheck",
               'NSIDC GHRC': "http://ghrc.nsstc.nasa.gov/hydro/ghost.xml",
               'NSIDC'     : "http://nsidc.org/data/polaris/api/opensearch/1.0/dataset.xml",
               'Mirador'   : "http://mirador.gsfc.nasa.gov/mirador_dataset_opensearch.xml",
               'ECHO1'     : "https://api.echo.nasa.gov/opensearch/datasets/descriptor_document.xml?clientId=CWICcheck",
               'ECHO2'     : "https://api.echo.nasa.gov/opensearch/datasets/descriptor_document.xml?clientId=CWICcheck",
               'WSNEWS'    : "http://wsnews.jpl.nasa.gov:8100/opensearch/osdd_dataset",
               'PODAAC'    : "http://podaac.jpl.nasa.gov:8890/ws/search/podaac-dataset-osd.xml",
               'FedEO'     : "http://geo.spacebel.be/opensearch/description.xml",
               'EUMETSAT'  : "http://rs211980.rs.hosteurope.de/mule/os-description/",
               }

usage = """[-u|--url <site URL> -v|--verbose <level>]
        -v full     Show all output (default)
        -v headers  Show HTTP response header only
        -v response Show XML response only
        -v feed     Run tests on <feed> elements response only
        -v paging   Run tests on paging hyperlinks in <feed> only
        -v entry    Run tests on <entry> elements only
        """

def osddTests(siteName,testUrl,expectedStatusCode,verbose):
    """ Run all of the tests for a given site and URL and print results."""
    # Loop over the list of URLs to test
    print "Test %s" % siteName
    
    # Parse the incoming URL to get all of the parameters and store them locally
    urlParms = parseUrl(testUrl)
    queryParms = {}
    if (urlParms.query):
        queryParms = parseQuery(urlParms.query)

    if queryParms:
        # Get datasetId
        if 'datasetId' in queryParms:
            theDatasetId = queryParms['datasetId'][0]
        else:
            theDatasetId = None

        # Get clientId
        if 'clientId' in queryParms:
            theClientId = queryParms['clientId'][0]
        else:
            theClientId = None

    # Send the URL off for a response
    try:
        response = requests.get(testUrl)
    except:
        print "*FAIL* Could not get response."
        print " "
        return
    
    # Evaluate the response
    if (verbose == "full" or verbose == "headers"):    # The HTTP return status should be 200 for success
        if (testStatus(expectedStatusCode,response)):
            print "%s: Got expected HTTP Status Code %s" % (siteName,expectedStatusCode)
        else:
            print "%s: Failed to get expected HTTP Status Code %s - got %s" % (siteName, expectedStatusCode, response.status_code)
            
        # Print out the HTTP header
        print "%s Header:" % siteName
        headers = response.headers
        for headerKey in headers:
            print "\t%s:%s" % (headerKey,headers[headerKey])
        if (verbose == "headers"):
            return
        print "\tencoding:%s" % response.encoding

    # Done with retrieving the URL, now set up for the XML tests by parsing the XML response
    rootTree = runOnce(response.content)
    
    # Check that the root tree is present
    if rootTree is None:
        print "*FAIL* %s: Failed to get valid XML response" % siteName
        return
    
    if (verbose == "full" or verbose == "response"):
        # Check that we got a valid Atom response back
        if testOsddElement(rootTree):
            print "%s: Got valid OSDD Response" % siteName
        else:
            print "%s: Got bad OSDD Response" % siteName
        if (verbose == "response"):
            return
        print " "
        printResponse(rootTree)

    if (verbose == "full" or verbose == "osdd"):
        testResults = testShortNameElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testDescriptionElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testTagsElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testContactElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testImageElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testDeveloperElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testAttributionElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testSyndicationRightElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testLanguageElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testOutputEncodingElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testInputEncodingElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testUrlElement(rootTree)
        printResults(siteName,testResults)
    
        testResults = testUrlParameterElements(rootTree)
        printResults(siteName,testResults)
    
    print " "
    return


def osddRunner(siteName,testUrl,verbose):
    expectedStatusCode = 200
    osddTests(siteName,testUrl,expectedStatusCode,verbose)


def main(argv):
    """ Run all of the tests against either the default list of sites or with the site given on the command line."""

    # Grab the test name and URL from the command line and run the tests on that
    siteName = None
    siteUrl  = None
    verbose  = "full"

    if argv: # If something is on the command line
        # Parse the command line
        try:
            opts, args = getopt.getopt(argv,"hn:u:v:",["name=","url=","verbose="])
        except getopt.GetoptError: # Got something unrecognized, so bail out
            print 'RunTests.py %s' % usage
            sys.exit(2)
        # Grab any options that are there
        for opt, arg in opts:
            if opt == '-h':
                print 'OSDD.py %s' % usage
                sys.exit()
            elif opt in ("-u", "--url"):
                siteName = "Command Line"
                siteUrl = arg
            elif opt in ("-v", "--verbose"):
                verbose = arg
                
    # Run one test if URL given on command line.  Otherwise, run the defaults
    if siteUrl:
        osddRunner(siteName, siteUrl,verbose)
    else: # or just run the defaults
        print "Running default tests"
        for key,value in sorted(urls.items()):
            osddRunner(key,value,verbose)
            print " "
        print "Done."
        sys.exit()

    print "Done."

# Set up the default function
if __name__ == "__main__":
     main(sys.argv[1:])