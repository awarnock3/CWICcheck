from lxml import etree

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         "geo":          "http://a9.com/-/opensearch/extensions/geo/1.0/",
         "time":         "http://a9.com/-/opensearch/extensions/time/1.0/",
         }

def testFeedElement(root):
    # Look for <feed> element to start
    if (root.tag == "{http://www.w3.org/2005/Atom}feed"):
        return "PASS"
    return "FAIL"


def testTitleElement(root):
    node = root.find("./atom:title",namespaces=nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found feed/title"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <title> element is found, make sure it's not empty
        testName = "feed/title not empty"
        if node.text:
            testResults[testName] = "PASS"

            # Since the <title> element isn't empty, check that we get the expected value
            testName = "Found CWIC title"
            if ("CWIC" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <title>
                testResults[testName] = "FAIL"
        else: # <title> element was empty
            testResults[testName] = "FAIL"
    else: # <title> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testUpdatedElement(root):
    node = root.find("./atom:updated",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/updated"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/updated not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testAuthorElement(root):
    node = root.find("./atom:author",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testAuthorNameElement(root):
    node = root.find("./atom:author/atom:name",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/name"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/author/name not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testAuthorEmailElement(root):
    node = root.find("./atom:author/atom:email",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/email"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/author/email not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testIdElement(root):
    node = root.find("./atom:id",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/id"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/id not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testSelfLinkElement(root):
    node = root.find("./atom:link[@rel='self']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/link[@rel='self']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found feed/link[@rel='self'][@href]"
    href = node.get("href")
    if (href is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found feed/link[@rel='self'][@type]"
    href = node.get("type")
    if (href is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found feed/link[@rel='self'][@title]"
    href = node.get("title")
    if (href is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testSearchLinkElement(root):
    node = root.find("./atom:link[@rel='search']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/link[@rel='search']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found link[@rel='search'][@href]"
    linkHref = node.get("href")
    if (linkHref is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found feed/link[@rel='search'][@type]"
    linkType = node.get("type")
    if (linkType is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    
    testName = "Found feed/link[@rel='search'][@title]"
    linkTitle = node.get("title")
    if (linkTitle is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testQueryElement(root):
    node = root.find("./opensearch:Query",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/Query"
    if (node is not None):
        testResults[testName] = "PASS"

        testName = "Found feed/Query[@role]"
        roleNode = root.find("./opensearch:Query[@role]",namespaces=nsmap)
        if (roleNode is not None):
            testResults[testName] = "PASS"

            testName = "Got correct feed/Query[@role] value"
            roleText = roleNode.get("role")
            if (roleText == "request"):
                testResults[testName] = "PASS"
            else:
                testResults[testName] = "FAIL"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@startPage]"
        pageNode = root.find("./opensearch:Query[@startPage]",namespaces=nsmap)
        if (pageNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@count]"
        countNode = root.find("./opensearch:Query[@count]",namespaces=nsmap)
        if (countNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@cwic:datasetId]"
        datasetNode = root.find("./opensearch:Query[@cwic:datasetId]",namespaces=nsmap)
        if (datasetNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@geo:box]"
        geoboxNode = root.find("./opensearch:Query[@geo:box]",namespaces=nsmap)
        if (geoboxNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@time:start]"
        timestartNode = root.find("./opensearch:Query[@time:start]",namespaces=nsmap)
        if (timestartNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        testName = "Found feed/Query[@time:end]"
        timestartNode = root.find("./opensearch:Query[@time:end]",namespaces=nsmap)
        if (timestartNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"       

    else:
        testResults[testName] = "FAIL"
    return testResults
  
