from lxml import etree
from CwicCheckUtils import *

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         "geo":          "http://a9.com/-/opensearch/extensions/geo/1.0/",
         "time":         "http://a9.com/-/opensearch/extensions/time/1.0/",
         }

def testFeedElement(root):
    """ Check that the root <feed> element is present."""
    # Look for <feed> element to start
    if (root.tag == "{http://www.w3.org/2005/Atom}feed"):
        return "PASS"
    return "FAIL"


def testTitleElement(root):
    """ Test that the feed <title> element is present and not empty, and that it contains the 
        correct CWIC title
        """
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
    """Check that the feed <updated> element is present and not empty."""
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
    """Check that the feed <author> element is present."""
    node = root.find("./atom:author",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/author/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testAuthorNameElement(root):
    """ Check that the <name> element in <author> is present and not empty."""
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
    """ Check that the <email> element in <author> is present and not empty."""
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
    """ Check that the feed <id> element is present and not empty."""
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
    """ Check that the feed <link rel='self'...> element is present and has the 
        correct attributes href, type and title
        """
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
    """ Check that the feed <link rel='search'> element is present and has
        the required attributes href, type and title.
        """
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
    """ Check that the feed <Query...> element is present and has all of the right
        attributes and values.
        """
    # TODO - check values against the requested values
    node = root.find("./opensearch:Query",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/Query"
    if (node is not None):
        testResults[testName] = "PASS"

        # Check that the role attribute is present and has the value of 'request'
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

        # Check that the startPage attribute is present
        testName = "Found feed/Query[@startPage]"
        pageNode = root.find("./opensearch:Query[@startPage]",namespaces=nsmap)
        if (pageNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        # Check that the count attribute is present
        testName = "Found feed/Query[@count]"
        countNode = root.find("./opensearch:Query[@count]",namespaces=nsmap)
        if (countNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        # Check that the datasetId attribute is present
        testName = "Found feed/Query[@cwic:datasetId]"
        datasetNode = root.find("./opensearch:Query[@cwic:datasetId]",namespaces=nsmap)
        if (datasetNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        # Check that the geo:box attribute is present
        testName = "Found feed/Query[@geo:box]"
        geoboxNode = root.find("./opensearch:Query[@geo:box]",namespaces=nsmap)
        if (geoboxNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        # Check that the time:start attribute is present
        testName = "Found feed/Query[@time:start]"
        timestartNode = root.find("./opensearch:Query[@time:start]",namespaces=nsmap)
        if (timestartNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

        # Check that the time:end attribute is present
        testName = "Found feed/Query[@time:end]"
        timeendNode = root.find("./opensearch:Query[@time:end]",namespaces=nsmap)
        if (timeendNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"       

        # Check that the esipdiscover:clientId attribute is present
        testName = "Found feed/Query[@esipdiscover:clientId]"
        clientIdNode = root.find("./opensearch:Query[@esipdiscover:clientId]",namespaces=nsmap)
        if (clientIdNode is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "WARN"       

    else:
        testResults[testName] = "FAIL"
    return testResults
  

def testAllFeed(rootTree,siteName):
    """ Run all of the tests on the <feed> element and required contents."""
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

    return