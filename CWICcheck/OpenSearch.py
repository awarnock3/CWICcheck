import sys
import requests
from UrlUtils import *
from ValidOpensearchFeedTests import *
from ValidOpensearchPagingTests import *
from ValidOpensearchEntryTests import *

urls = {'INPE':       'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=5&clientId=CWICcheck',
        'USGS/LSI':   'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        }

# Print out the test results in a fixed format
def printResults(name,testResults):
    """ Print all of the test results passed in for the named site."""
    # Walk the testResults array and print the results for each test
    if testResults:
        for testName in testResults:
            print "*%s* %s: Test \'%s\'" % (testResults[testName],name,testName)
    else:
        print "*FAIL* %s: No test results found" % name

# Run this one time to parse the XML into an ElementTree
def runOnce(xmlResponse):
    """ Run one time at the start of the test.
        This parses the XML response into the tree object for later processing with lxml
        """
    # Check that we can parse the XML response string
    try:
        root = etree.fromstring(xmlResponse)
    except:
        print "*FAIL* Could not parse response"
        print "Got: "
        print xmlResponse
        print " "
        return
    return root


# Pretty-print out the returned response
def printResponse(root):
    # If we can parse it, try to print a nice version of it out
    try:
        print(etree.tostring(root, pretty_print="PASS"))
    except:
        print "*FAIL* Could not parse document to print"
        print " "
        return
    return root


# Runs all of the tests on a URL
def openSearchTests(siteName,testUrl,verbose):
    """ Run all of the tests for a given site and URL and print results."""
    # Loop over the list of URLs to test
    print "Testing site %s" % siteName
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
      

    if (verbose == "full" or verbose == "headers"):    # Check the HTTP return status - it should be 200 for success
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
        # Check for the feed title element and contents
        print " "
        print "Feed tests"
    
        # Check the feed <title> element
        testResults = testTitleElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <updated> element
        testResults = testUpdatedElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <author> element
        testResults = testAuthorElement(rootTree)
        printResults(siteName,testResults)

        # Check the <name> element inside of the feed <author> element
        testResults = testAuthorNameElement(rootTree)
        printResults(siteName,testResults)

        # Check the <email> element inside of the feed <author> element
        testResults = testAuthorEmailElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <id> element
        testResults = testIdElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <link rel='self'...> element
        testResults = testSelfLinkElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <link rel='search'...> element
        testResults = testSearchLinkElement(rootTree)
        printResults(siteName,testResults)

        # Check the feed <Query> element
        testResults = testQueryElement(rootTree)
        printResults(siteName,testResults)
        
        if (verbose == "feed"):
            return

    if (verbose == "full" or verbose == "paging"):
        # Now run the hypermedia pagination tests
        print " "
        print "Paging tests"
        testResults = testPaging(rootTree,requestedStartPage=theStartPage,requestedCount=theCount)
        printResults(siteName,testResults)

        if (verbose == "paging"):
            return
    
    if (verbose == "full" or verbose == "entry"):
        # Run the tests on the <entry> element
        print " "
        print "Entry Tests"
        # Check if we got any <entry> elements returned
        numEntries = computeEntryCount(rootTree)
        print "Found %s returned <entry> elements" % numEntries
    
        # If so, see if the first <entry> has all of the expected elements
        if (numEntries > 0):
            # Check the feed <entry> element
            testResults = testEntryElement(rootTree)
            printResults(siteName,testResults)

            # Check the <title> element inside of the feed <entry> element
            testResults = testEntryTitleElement(rootTree)
            printResults(siteName,testResults)

            # Check the <id> element inside of the feed <entry> element
            testResults = testEntryIdElement(rootTree)
            printResults(siteName,testResults)

            # Check the <updated> element inside of the feed <entry> element
            testResults = testEntryUpdatedElement(rootTree)
            printResults(siteName,testResults)

            # Check the <author> element inside of the feed <entry> element
            testResults = testEntryAuthorElement(rootTree)
            printResults(siteName,testResults)

            # Check the <name> element inside of the feed <entry>/<author> element
            testResults = testEntryAuthorNameElement(rootTree)
            printResults(siteName,testResults)

            # Check the <email> element inside of the feed <entry>/<author> element
            testResults = testEntryAuthorEmailElement(rootTree)
            printResults(siteName,testResults)

            # Check the <geo:box> element inside of the feed <entry> element
            testResults = testEntryBoxElement(rootTree)
            printResults(siteName,testResults)

            # Check the <dc:date> element inside of the feed <entry> element
            testResults = testEntryDateElement(rootTree)
            printResults(siteName,testResults)

            # Check the <link rel='via'...> element inside of the feed <entry> element
            testResults = testEntryViaLinkElement(rootTree)
            printResults(siteName,testResults)

            # Check the <link rel='icon'...> element inside of the feed <entry> element
            testResults = testEntryIconLinkElement(rootTree)
            printResults(siteName,testResults)

            # Check the <link rel='alt'> element inside of the feed <entry> element
            testResults = testEntryAltLinkElement(rootTree)
            printResults(siteName,testResults)

        else:
            # If we got no <entry> elements returned, make sure we didn't expect to get any
            print "Got no returned entries."
            testResults = testNoExpectedEntries(rootTree,requestedStartPage=theStartPage,requestedCount=theCount)
            printResults(siteName,testResults)
        
    print " "

# Loops over the list of URLS and runs the tests on each
def runner():
    for key,value in urls.iteritems():
        openSearchTests(key,value)

# Sets the default function
if __name__ == "__main__":
    runner()