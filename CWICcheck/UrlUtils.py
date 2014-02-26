from urlparse import urlparse,parse_qs

# Compare the HTTP status code with the expected value
def testStatus(expectedCode,response):
    if (response.status_code == expectedCode):
        return True
    return False

# Parse out the individual query parameters and values
def parseQuery(queryString):
    queryParms = parse_qs(queryString)
    return queryParms

# Parse the URL into its components
def parseUrl(url):
    urlParms = urlparse(url)
    return urlParms
