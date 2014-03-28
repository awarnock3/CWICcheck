import sys
import requests
from CwicCheckUtils import *
from UrlUtils import *
from ValidOsddTests import *

osdds = {'Valid':        "http://cwictest.wgiss.ceos.org/opensearch/datasets/Landsat_8/osdd.xml?clientId=CWICcheck",
         'NoClientId':   "http://cwictest.wgiss.ceos.org/opensearch/datasets/Landsat_8/osdd.xml",
         'NoDatasetId':  "http://cwictest.wgiss.ceos.org/opensearch/datasets/osdd.xml?clientId=CWICcheck",
         'NoParameters': "http://cwictest.wgiss.ceos.org/opensearch/datasets/osdd.xml",
         'BadDataset':   "http://cwictest.wgiss.ceos.org/opensearch/datasets/foobar/osdd.xml",
         }

def osddTests(siteName,testUrl,verbose):
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
        expectedStatusCode = 200
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
        if testOsddResponse(rootTree):
            print "%s: Got valid OSDD Response" % siteName
        else:
            print "%s: Got bad OSDD Response" % siteName
        if (verbose == "response"):
            return
        print " "
        printResponse(rootTree)

    print " "
    return


# Loops over the list of URLS and runs the tests on each
def osddRunner():
    verbose = "full"
    for key,value in sorted(osdds.items()):
        osddTests(key,value,verbose)

# Sets the default function
if __name__ == "__main__":
    osddRunner()