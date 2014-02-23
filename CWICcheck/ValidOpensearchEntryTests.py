from lxml import etree

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         }

def testEntryElement(root):
    node = root.find("./atom:entry",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False

    return testResults
