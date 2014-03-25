from lxml import etree
from CwicCheckUtils import *

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         "georss":       "http://www.georss.org/georss/10",
         "dc":           "http://purl.org/dc/elements/1.1/",
         }

def computeEntryCount(root):
    """ Compute the number of <entry> elements returned."""
    count_elements = etree.XPath("count(//*[local-name() = $name])")
    nEntries = count_elements(root, name = "entry")
    if (nEntries):
        return int(nEntries)
    else:
        return 0

    
def testNoExpectedEntries(root,requestedStartPage, requestedCount):
    """ Check if we got back no entries if we are at or past the last page of results."""
    nEntries = computeEntryCount(root)
    testResults = {}
    node = root.find("./opensearch:totalResults",namespaces=nsmap)
    totalResults=int(node.text)
    if (int(requestedStartPage) * int(requestedCount) > totalResults):
        testName = "No entries expected"
        if (nEntries > 0):
            testResults[testName] = "FAIL"
        else:
            testResults[testName] = "PASS"
    else:
        testName = "Expected entries returned"
        testResults[testName] = "FAIL"
    return testResults


def testEntryElement(root):
    """ Check if we found a first <entry> element."""
    node = root.find("./atom:entry[1]",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testEntryTitleElement(root):
    """ Check if we found a <title> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:title",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/title"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/title not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testEntryUpdatedElement(root):
    """ Check if we found a <updated> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:updated",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/updated"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/updated not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testEntryAuthorElement(root):
    """ Check if we found a <author> element in the first <entry>."""
    node = root.find("./atom:entry[1]/atom:author",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/author/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testEntryAuthorNameElement(root):
    """ Check that the <author> element in the first <entry> has a <name> element and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:author/atom:name",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/author/name"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/author/name not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testEntryAuthorEmailElement(root):
    """ Check that the <author> element in the first <entry> has an <email> element and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:author/atom:email",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/author/email"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/author/email not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testEntryIdElement(root):
    """ Check if we found a <id> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:id",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/id"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/id not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    return testResults


def testEntryBoxElement(root):
    """ Check if we found a <georss:box> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/georss:box",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/georss:box/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
        
    if (node is not None):
        testName = "feed/entry/georss:box not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

    return testResults


def testEntryDateElement(root):
    """ Check if we found a <dc:date> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/dc:date",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/dc:date/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    if (node is not None):
        testName = "feed/entry/dc:date not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    
    return testResults


def testEntryViaLinkElement(root):
    """ Check if we found a <link rel='via'> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:link[@rel='via']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='via']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"

    if (node is not None):
        testName = "feed/entry/link[@rel='via'] not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

    return testResults


def testEntryIconLinkElement(root):
    """ Check if we found a <link rel='icon'> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:link[@rel='icon']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='icon']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"
        
    if (node is not None):
        testName = "feed/entry/link[@rel='icon'] not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

    return testResults


def testEntryAltLinkElement(root):
    """ Check if we found a <link rel='alternate'> element in the first <entry> and that it is not empty."""
    node = root.find("./atom:entry[1]/atom:link[@rel='alternate'][1]",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='alternate']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"
        
    if (node is not None):
        testName = "feed/entry/link[@rel='alternate'] not empty"
        if node.text:
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"

    return testResults


def testAllEntry(rootTree,siteName):
    """ Run tests on all of the required elements inside of <entry>"""
    # Check the feed <entry> element
    testResults = testEntryElement(rootTree)
    printResults(siteName,testResults)

    # Check the <title> element inside of the feed <entry> element
    testResults = testEntryTitleElement(rootTree)
    printResults(siteName,testResults)

    # Check the <id> element inside of the feed <entry> element
    testResults = testEntryIdElement(rootTree)
    printResults(siteName,testResults)

    # Check the <updated> element inside of the feed <entry> element
    testResults = testEntryUpdatedElement(rootTree)
    printResults(siteName,testResults)

    # Check the <author> element inside of the feed <entry> element
    testResults = testEntryAuthorElement(rootTree)
    printResults(siteName,testResults)

    # Check the <name> element inside of the feed <entry>/<author> element
    testResults = testEntryAuthorNameElement(rootTree)
    printResults(siteName,testResults)

    # Check the <email> element inside of the feed <entry>/<author> element
    testResults = testEntryAuthorEmailElement(rootTree)
    printResults(siteName,testResults)

    # Check the <geo:box> element inside of the feed <entry> element
    testResults = testEntryBoxElement(rootTree)
    printResults(siteName,testResults)

    # Check the <dc:date> element inside of the feed <entry> element
    testResults = testEntryDateElement(rootTree)
    printResults(siteName,testResults)

    # Check the <link rel='via'...> element inside of the feed <entry> element
    testResults = testEntryViaLinkElement(rootTree)
    printResults(siteName,testResults)

    # Check the <link rel='icon'...> element inside of the feed <entry> element
    testResults = testEntryIconLinkElement(rootTree)
    printResults(siteName,testResults)

    # Check the <link rel='alt'> element inside of the feed <entry> element
    testResults = testEntryAltLinkElement(rootTree)
    printResults(siteName,testResults)

    return