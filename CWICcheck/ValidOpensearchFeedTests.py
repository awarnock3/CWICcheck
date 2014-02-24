from lxml import etree

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         }

# Run this one time to parse the XML into an ElementTree
def runOnce(xmlResponse):
  root = etree.fromstring(xmlResponse)
  print(etree.tostring(root, pretty_print=True))
  return root

def testFeedElement(root):
  # Look for <feed> element to start
  if (root.tag == "{http://www.w3.org/2005/Atom}feed"):
    return True
  return False

def testTitleElement(root):
    node = root.find("./atom:title",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/title"
    if (node is not None):
      testResults[testName] = True
      
      testName = "feed/title not empty"
      if node.text:
        testResults[testName] = True
      else:
        testResults[testName] = False
    
      testName = "Found CWIC title"
      if ("CWIC" in node.text):
        testResults[testName] = True
      else:
        testResults[testName] = False
    else:
      testResults[testName] = False
    return testResults
    
def testUpdatedElement(root):
    node = root.find("./atom:updated",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/updated"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
      
    if (node is not None):
      testName = "feed/updated not empty"
      if node.text:
        testResults[testName] = True
      else:
        testResults[testName] = False
    return testResults

def testAuthorElement(root):
    node = root.find("./atom:author",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    return testResults

def testAuthorNameElement(root):
    node = root.find("./atom:author/atom:name",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/name"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
      
    if (node is not None):
      testName = "feed/author/name not empty"
      if node.text:
        testResults[testName] = True
      else:
        testResults[testName] = False
    return testResults

def testAuthorEmailElement(root):
    node = root.find("./atom:author/atom:email",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/email"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
      
    if (node is not None):
      testName = "feed/author/email not empty"
      if node.text:
        testResults[testName] = True
      else:
        testResults[testName] = False
    return testResults

def testIdElement(root):
    node = root.find("./atom:id",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/id"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
      
    if (node is not None):
      testName = "feed/id not empty"
      if node.text:
        testResults[testName] = True
      else:
        testResults[testName] = False
    return testResults
  
def testSelfLinkElement(root):
    node = root.find("./atom:link[@rel='self']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/link[@rel='self']"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found feed/link[@rel='self'][@href]"
    href = node.get("href")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found feed/link[@rel='self'][@type]"
    href = node.get("type")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found feed/link[@rel='self'][@title]"
    href = node.get("title")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    return testResults
  
def testSearchLinkElement(root):
    node = root.find("./atom:link[@rel='search']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/link[@rel='search']"
    if (node is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found link[@rel='search'][@href]"
    href = node.get("href")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found feed/link[@rel='search'][@type]"
    href = node.get("type")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    
    testName = "Found feed/link[@rel='search'][@title]"
    href = node.get("title")
    if (href is not None):
      testResults[testName] = True
    else:
      testResults[testName] = False
    return testResults

def testQueryElement(root):
    node = root.find("./opensearch:Query",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/Query"
    if (node is not None):
      testResults[testName] = True
    
      testName = "Found Query[@role]"
      roleNode = root.find("./opensearch:Query[@role]",namespaces=nsmap)
      if (roleNode is not None):
        testResults[testName] = True
        
#        testName = "Got correct role value"
#        role = roleNode.text
#        print "@role=%s" % role
#        if (role == "request"):
#          testResults[testName] = True
#        else:
#          testResults[testName] = False
      else:
        testResults[testName] = False
      
    else:
      testResults[testName] = False
    return testResults
  
