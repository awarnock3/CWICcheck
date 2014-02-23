import requests
from UrlUtils import testStatus
from ValidOsddTests import isOsddResponse

osdds = {'Valid': "http://cwictest.wgiss.ceos.org/opensearch/datasets.atom?datasetId=LANDSAT_8&clientId=CWICcheck",
         'NoClientId': "http://cwictest.wgiss.ceos.org/opensearch/datasets.atom",
         'NoDatasetId': "http://cwictest.wgiss.ceos.org/opensearch/datasets.atom?clientId=CWICcheck"
         }

    
for key,value in osdds.iteritems():
    response = requests.get(value)
    expectedStatusCode = 200
    if (testStatus(expectedStatusCode,response)):
        print "%s: Got expected HTTP Status Code %s" % (key,expectedStatusCode)
    else:
      print "%s: Failed to get expected HTTP Status Code %s - got %s" % (key, expectedStatusCode, response.status_code)

    print "%s Header:" % key
    print "\tContent-Type:", response.headers['content-type']
    print "\tDate:", response.headers['date']
    print "\tServer:", response.headers['server']

    if (isOsddResponse):
      print "%s: Got valid Atom Response" % key
    else:
      print "%s: Got bad Atom Response" % key
    print " "
