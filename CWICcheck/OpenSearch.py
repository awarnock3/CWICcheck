import requests
from UrlUtils import *
from ValidOpensearchFeedTests import *
from ValidOpensearchPagingTests import *
from ValidOpensearchEntryTests import *

urls = {'INPE': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=5&clientId=CWICcheck',
        'USGS/LSI': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'GHRSST': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'NASA/ECHO': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=GES_DISC_TRMM_G2A12_V6&startPage=1&count=5&timeStart=1997-12-07T00:00:00Z&timeEnd=1997-12-14T00:00:00Z&geoBox=-180,-38,180,38&clientId=CWICcheck',
        }

def printResults(name,testResults):
  # Walk the testResults array and print the results for each test
  if testResults:
    for testName in testResults:
      if testResults[testName]:
        print "*PASS* %s: Test \'%s\' passed" % (name,testName)
      else:
        print "*FAIL* %s: Test \'%s\' failed" % (name,testName)
  else:
    print "*FAIL* %s: No feed <title> element found" % name

def openSearchTests():
  # Loop over the list of URLs to test  
  for key,value in urls.iteritems():
    # Send the URL off for a response
    response = requests.get(value)

    # Parse the URL to get all of the parameters
    #  print "Request URL: %s" % value
    urlParms = parseUrl(value)
    
    if (urlParms.query):
      queryParms = parseQuery(urlParms.query)

    #print "urlParms   =",urlParms
    #print "queryParms =",queryParms
    #print " "
  
    # Check the HTTP return status - it should be 200 for success
    expectedStatusCode = 200
    if (testStatus(expectedStatusCode,response)):
      print "*PASS* %s: Got expected HTTP Status Code %s" % (key,expectedStatusCode)
    else:
      print "*FAIL* %s: Failed to get expected HTTP Status Code %s - got %s" % (key, expectedStatusCode, response.status_code)

    # Print out the HTTP header
    print "%s Header:" % key
    print "\tContent-Type:", response.headers['content-type']
    print "\tDate:", response.headers['date']
    print "\tServer:", response.headers['server']

    # Done with retrieving the URL, now set up for the XML tests
    rootTree = runOnce(response.content)

    # Check that we got a valid Atom response back
    if (testFeedElement(rootTree)):
      print "*PASS* %s: Got valid Atom Response" % key
    else:
      print "*FAIL* %s: Got bad Atom Response" % key
    
    # Check for the feed title element and contents
    testResults = testTitleElement(rootTree)
    printResults(key,testResults)

    testResults = testUpdatedElement(rootTree)
    printResults(key,testResults)
    
    testResults = testAuthorElement(rootTree)
    printResults(key,testResults)

    testResults = testAuthorNameElement(rootTree)
    printResults(key,testResults)

    testResults = testAuthorEmailElement(rootTree)
    printResults(key,testResults)

    testResults = testIdElement(rootTree)
    printResults(key,testResults)

    testResults = testSelfLinkElement(rootTree)
    printResults(key,testResults)

    testResults = testSearchLinkElement(rootTree)
    printResults(key,testResults)

    testResults = testPaging(rootTree)
    printResults(key,testResults)

    testResults = testQueryElement(rootTree)
    printResults(key,testResults)

    testResults = testEntryElement(rootTree)
    printResults(key,testResults)

    print " "

if __name__ == "__main__":
  openSearchTests()