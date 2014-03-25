import sys
import requests
from CwicCheckUtils import *
from UrlUtils import *
from ValidOpensearchFeedTests import *
from ValidOpensearchPagingTests import *
from ValidOpensearchEntryTests import *

urls = {'INPE':       'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=5&clientId=CWICcheck',
        'USGS/LSI':   'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        }


def openSearchTests(siteName,testUrl,verbose):
    """ Run all of the tests for a given site and URL and print results."""
    # Loop over the list of URLs to test
    print "Test %s" % siteName
    
    # Parse the incoming URL to get all of the parameters and store them locally
    urlParms = parseUrl(testUrl)
    queryParams = {}
    if (urlParms.query):
        queryParms = parseQuery(urlParms.query)

    # Get startPage
    if 'startPage' in queryParms:
        theStartPage = queryParms['startPage'][0]
    else:
        theStartPage = None
        
    # Get number of hits requested
    if 'count' in queryParms:
        theCount = queryParms['count'][0]
    else:
        theCount = None
        
    # Get the client ID
    if 'clientId' in queryParms:
        theClientId = queryParms['clientId'][0]
    else:
        theClientId = None

    # Get the requested dataset ID
    if 'datasetId' in queryParms:
        theDatasetId = queryParms['datasetId'][0]
    else:
        theDatasetId = None

    # Get the requested search start time
    if 'timeStart' in queryParms:
        theTimeStart = queryParms['timeStart'][0]
    else:
        theTimeStart = None

    # Get the requested search end time
    if 'timeEnd' in queryParms:
        theTimeEnd = queryParms['timeEnd'][0]
    else:
        theTimeEnd = None

    # Get the requested spatial footprint
    if 'geoBox' in queryParms:
        theGeoBox = queryParms['geoBox'][0]
    else:
        theGeoBox = None
    
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
            print "*PASS* %s: Got expected HTTP Status Code %s" % (siteName,expectedStatusCode)
        else:
            print "*FAIL* %s: Failed to get expected HTTP Status Code %s - got %s" % (siteName, expectedStatusCode, response.status_code)
            print " "
            return

        # Print out the HTTP header
        print "%s Header:" % siteName
        headers = response.headers
        for headerKey in headers:
            print "\t%s:%s" % (headerKey,headers[headerKey])
        if (verbose == "headers"):
            return

    # Done with retrieving the URL, now set up for the XML tests by parsing the XML response
    rootTree = runOnce(response.content)
    
    # Check that the root tree is present
    if rootTree is None:
        print "*FAIL* %s: Failed to get valid XML response" % siteName
        return

    if (verbose == "full" or verbose == "response"):
        # Check that we got a valid Atom response back
        if (testFeedElement(rootTree)):
            print "*PASS* %s: Got valid Atom Response" % siteName
        else:
            print "*FAIL* %s: Got bad Atom Response" % siteName
            return
        printResponse(rootTree)
        if (verbose == "response"):
            return
    
    if (verbose == "full" or verbose == "feed"):
        # Check the required feed elements and contents
        print " "
        print "%s Feed tests" % siteName
        testAllFeed(rootTree,siteName)
                
        if (verbose == "feed"):
            return

    if (verbose == "full" or verbose == "paging"):
        # Check that the hypermedia pagination links are present
        print " "
        print "%s Paging tests" % siteName
        testResults = testPaging(rootTree,requestedStartPage=theStartPage,requestedCount=theCount)
        printResults(siteName,testResults)

        if (verbose == "paging"):
            return
    
    if (verbose == "full" or verbose == "entry"):
        # Run the tests on the <entry> element
        print " "
        print "%s Entry Tests" % siteName

        # Check if we got any <entry> elements returned
        numEntries = computeEntryCount(rootTree)
        print "Found %s returned <entry> elements" % numEntries
    
        # If so, see if the first <entry> has all of the expected elements
        if (numEntries > 0):
            # If there are entry elements, see if the first one has all of the expected elements
            testAllEntry(rootTree,siteName)
        else:
            # If we got no <entry> elements returned, make sure we didn't expect to get any
            print "Got no returned entries."
            testResults = testNoExpectedEntries(rootTree,requestedStartPage=theStartPage,requestedCount=theCount)
            printResults(siteName,testResults)
        
    print " "


# Loops over the list of URLS and runs the tests on each
def runner():
#    for key,value in urls.iteritems():
    for key,value in sorted(urls.items()):
        openSearchTests(key,value)

# Sets the default function
if __name__ == "__main__":
    runner()