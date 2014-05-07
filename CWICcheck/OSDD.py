import sys
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
               }

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


def validOsddTests(siteName,testUrl,verbose):
    expectedStatusCode = 200
    osddTests(siteName,testUrl,expectedStatusCode,verbose)
    

def invalidOsddTests(siteName,testUrl,verbose):
    expectedStatusCode = 400
    osddTests(siteName,testUrl,expectedStatusCode,verbose)
    

# Loops over the list of URLS and runs the tests on each
def osddRunner():
    verbose = "full"
    for key,value in sorted(valid_osdds.items()):
        validOsddTests(key,value,verbose)
        
    for key,value in sorted(invalid_osdds.items()):
        invalidOsddTests(key,value,verbose)

    for key,value in sorted(other_osdds.items()):
        invalidOsddTests(key,value,verbose)

# Sets the default function
if __name__ == "__main__":
    osddRunner()