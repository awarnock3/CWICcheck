import sys
import requests
from UrlUtils import *
from ValidOpensearchFeedTests import *
from ValidOpensearchPagingTests import *
from ValidOpensearchEntryTests import *

urls = {'INPE':       'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=5&clientId=CWICcheck',
        'USGS/LSI':   'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'GHRSST':     'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'NASA/ECHO':  'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=GES_DISC_TRMM_G2A12_V6&startPage=1&count=5&timeStart=1997-12-07T00:00:00Z&timeEnd=1997-12-14T00:00:00Z&geoBox=-180,-38,180,38&clientId=CWICcheck',
        'NASA/ECHO2': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&timeStart=2000-02-24T00:00:00Z&timeEnd=2014-02-19T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        }

# Print out the test results in a fixed format
def printResults(name,testResults):
    # Walk the testResults array and print the results for each test
    if testResults:
        for testName in testResults:
            print "*%s* %s: Test \'%s\'" % (testResults[testName],name,testName)
    else:
        print "*FAIL* %s: No test results found" % name

# Run this one time to parse the XML into an ElementTree
def runOnce(xmlResponse):
    # Check that we can parse the XML response string
    try:
        root = etree.fromstring(xmlResponse)
    except:
        print "*FAIL* Could not parse response"
        print "Got: "
        print xmlResponse
        print " "
        return

    # If we can parse it, try to print a nice version of it out
    try:
        print(etree.tostring(root, pretty_print="PASS"))
    except:
        print "*FAIL* Could not parse document to print"
        print " "
        return
    return root

# Runs all of the tests on a URL
def openSearchTests(siteName,testUrl):
    # Loop over the list of URLs to test
    print "Testing site %s" % siteName
    
    # Send the URL off for a response
    try:
        response = requests.get(testUrl)
    except:
        print "*FAIL* Could not get response."
        print " "
        return
      
    # Parse the URL to get all of the parameters
    #  print "Request URL: %s" % testUrl
    urlParms = parseUrl(testUrl)
#    print "urlParms=",urlParms
    
    queryParams = {}
    if (urlParms.query):
        queryParms = parseQuery(urlParms.query)

#    print "queryParms =",queryParms
#    print " "
    if 'startPage' in queryParms:
        theStartPage = queryParms['startPage'][0]
    else:
        theStartPage = None
        
    if 'count' in queryParms:
        theCount = queryParms['count'][0]
    else:
        theCount = None
        
    if 'clientId' in queryParms:
        theClientId = queryParms['clientId'][0]
    else:
        theClientId = None
        
    if 'datasetId' in queryParms:
        theDatasetId = queryParms['datasetId'][0]
    else:
        theDatasetId = None

    if 'timeStart' in queryParms:
        theTimeStart = queryParms['timeStart'][0]
    else:
        theTimeStart = None

    if 'timeEnd' in queryParms:
        theTimeEnd = queryParms['timeEnd'][0]
    else:
        theTimeEnd = None

    if 'geoBox' in queryParms:
        theGeoBox = queryParms['geoBox'][0]
    else:
        theGeoBox = None

        
    # Check the HTTP return status - it should be 200 for success
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

    # Done with retrieving the URL, now set up for the XML tests
    rootTree = runOnce(response.content)
    
    if rootTree is None:
        return

    # Check that we got a valid Atom response back
    if (testFeedElement(rootTree)):
        print "*PASS* %s: Got valid Atom Response" % siteName
    else:
        print "*FAIL* %s: Got bad Atom Response" % siteName
    
    # Check for the feed title element and contents
    print " "
    print "Feed tests"
    testResults = testTitleElement(rootTree)
    printResults(siteName,testResults)

    testResults = testUpdatedElement(rootTree)
    printResults(siteName,testResults)
    
    testResults = testAuthorElement(rootTree)
    printResults(siteName,testResults)

    testResults = testAuthorNameElement(rootTree)
    printResults(siteName,testResults)

    testResults = testAuthorEmailElement(rootTree)
    printResults(siteName,testResults)

    testResults = testIdElement(rootTree)
    printResults(siteName,testResults)

    testResults = testSelfLinkElement(rootTree)
    printResults(siteName,testResults)

    testResults = testSearchLinkElement(rootTree)
    printResults(siteName,testResults)

    testResults = testQueryElement(rootTree)
    printResults(siteName,testResults)

    print " "
    print "Paging tests"
    testResults = testPaging(rootTree,requestedStartPage=theStartPage,requestedCount=theCount)
    printResults(siteName,testResults)

    # Run the tests on the Entry element
    print " "
    print "Entry Tests"
    testResults = testEntryElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryTitleElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryIdElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryUpdatedElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryAuthorElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryAuthorNameElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryAuthorEmailElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryBoxElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryDateElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryViaLinkElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryIconLinkElement(rootTree)
    printResults(siteName,testResults)

    testResults = testEntryAltLinkElement(rootTree)
    printResults(siteName,testResults)

    print " "

# Loops over the list of URLS and runs the tests on each
def runner():
    for key,value in urls.iteritems():
        openSearchTests(key,value)

# Sets the default function
if __name__ == "__main__":
    runner()