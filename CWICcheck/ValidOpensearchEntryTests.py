from lxml import etree

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
    node = root.find("./atom:entry[1]/georss:box",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/georss:box/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testEntryDateElement(root):
    node = root.find("./atom:entry[1]/dc:date",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/dc:date/"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"
    return testResults


def testEntryViaLinkElement(root):
    node = root.find("./atom:entry[1]/atom:link[@rel='via']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='via']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"
    return testResults


def testEntryIconLinkElement(root):
    node = root.find("./atom:entry[1]/atom:link[@rel='icon']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='icon']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"
    return testResults


def testEntryAltLinkElement(root):
    node = root.find("./atom:entry[1]/atom:link[@rel='alternate'][1]",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/entry/link[@rel='alternate']"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "WARN"
    return testResults
