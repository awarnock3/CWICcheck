from lxml import etree
from CwicCheckUtils import *

def testOsddResponse(root):
    # Look for <feed> element to start
    if (root.tag == "{http://a9.com/-/spec/opensearch/1.1/}OpenSearchDescription"):
        return "PASS"
    return "FAIL"
