from urlparse import urlparse,parse_qs

def testStatus(expectedCode,response):
  if (response.status_code == expectedCode):
    return True
  return False

def parseQuery(queryString):
  queryParms = parse_qs(queryString)
  return queryParms

def parseUrl(url):
  urlParms = urlparse(url)
  return urlParms
