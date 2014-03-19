from lxml import etree

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         }

def testPaging(root, requestedStartPage, requestedCount):
    testResults = {}

    node = root.find("./opensearch:totalResults",namespaces=nsmap)
    testName = "Found feed/totalResults"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    totalResults=node.text
    
    node = root.find("./opensearch:startPage",namespaces=nsmap)
    testName = "Found feed/startPage"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    startPage=node.text
    if requestedStartPage:
        testName = "Returned startPage = requested startPage"
        if (requestedStartPage == startPage):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "WARN"
    
    node = root.find("./opensearch:itemsPerPage",namespaces=nsmap)
    testName = "Found feed/itemsPerPage"
    if (node is not None):
        testResults[testName] = "PASS"
    else:
        testResults[testName] = "FAIL"

    itemsPerPage=node.text
    if requestedCount:
        testName = "Returned expected itemsPerPage = requested count"
        if (requestedCount == itemsPerPage):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "WARN"
    
    # Calculate number of pages
    numPages = 0
    if int(itemsPerPage) > 0:
        numPages = int(totalResults)/int(requestedCount)
        if (int(totalResults) % int(requestedCount) > 0):
            numPages += 1
        #print "totalResults=%s, requestedCount=%s, itemsPerPage=%s, numPages=%d" % (totalResults,requestedCount,itemsPerPage,numPages)
    
    # Look for first link
    node = root.find("./atom:link[@rel='first']",namespaces=nsmap)
    testName = "Found feed/link[@rel='first']"
    if (node is not None):
        testResults[testName] = "PASS"

        testName = "Found feed/link[@rel='first'][@href]"
        href = node.get("href")
        if (href is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    else:
        testResults[testName] = "FAIL"

    # If startPage > 1, look for prev link
    if (int(startPage) > 1):
        node = root.find("./atom:link[@rel='previous']",namespaces=nsmap)
        testName = "Found feed/link[@rel='previous']"
        if (node is not None):
            testResults[testName] = "PASS"
            testName = "Found feed/link[@rel='previous'][@href]"
            href = node.get("href")
            if (href is not None):
                testResults[testName] = "PASS"
            else:
                testResults[testName] = "FAIL"
        else:
            testResults[testName] = "FAIL"
    else: # If startPage is <= 1, no "previous" link should appear
        node = root.find("./atom:link[@rel='previous']",namespaces=nsmap)
        testName = "Omit feed/link[@rel='previous'] on first page"
        if (node is not None):
            testResults[testName] = "FAIL"
        else:
            testResults[testName] = "PASS"
    
    # If startPage < number of pages, look for next link
    #print "startPage=%s, numPages=%d" % (startPage,numPages)
    if (int(startPage) < numPages):
        node = root.find("./atom:link[@rel='next']",namespaces=nsmap)
        testName = "Found feed/link[@rel='next']"
        if (node is not None):
            testResults[testName] = "PASS"
            testName = "Found feed/link[@rel='next'][@href]"
            href = node.get("href")
            if (href is not None):
                testResults[testName] = "PASS"
            else:
                testResults[testName] = "FAIL"
        else:
            testResults[testName] = "FAIL"
    else: # If startPage >= number of pages, no "next" link should appear
        node = root.find("./atom:link[@rel='next']",namespaces=nsmap)
        testName = "Omit feed/link[@rel='next'] on last page"
        if (node is not None):
            testResults[testName] = "FAIL"
        else:
            testResults[testName] = "PASS"
    
    # Look for last link with correct number of pages
    node = root.find("./atom:link[@rel='last']",namespaces=nsmap)
    testName = "Found feed/link[@rel='last']"
    if (node is not None):
        testResults[testName] = "PASS"
        testName = "Found feed/link[@rel='last'][@href]"
        href = node.get("href")
        if (href is not None):
            testResults[testName] = "PASS"
        else:
            testResults[testName] = "FAIL"
    else:
        testResults[testName] = "FAIL"

    return testResults
