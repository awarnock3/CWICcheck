from lxml import etree

nsmap = {None:           "http://www.w3.org/2005/Atom",
         "atom":         "http://www.w3.org/2005/Atom",
         "opensearch":   "http://a9.com/-/spec/opensearch/1.1/",
         "cwic":         "http://cwic.wgiss.ceos.org/opensearch/extensions/1.0/",
         "esipdiscover": "http://commons.esipfed.org/ns/discovery/1.2/",
         }

def testPaging(root):
    node = root.find("./opensearch:totalResults",namespaces=nsmap)
    testResults = {}
    testName = "Found <totalResults>"
    if (node is not None):
      testResults[testName] = "PASS"
    else:
      testResults[testName] = "FAIL"

    totalResults=node.text
    
    node = root.find("./opensearch:startPage",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/startPage"
    if (node is not None):
      testResults[testName] = "PASS"
    else:
      testResults[testName] = "FAIL"

    startPage=node.text
    
    node = root.find("./opensearch:itemsPerPage",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/itemsPerPage"
    if (node is not None):
      testResults[testName] = "PASS"
    else:
      testResults[testName] = "FAIL"

    itemsPerPage=node.text
    
    # Calculate number of pages
    numPages = int(float(totalResults)/float(itemsPerPage) + 0.5)
    #print "numPages=",numPages
    
    # Look for first link
    node = root.find("./atom:link[@rel='first']",namespaces=nsmap)
    testResults = {}
    testName = "Found feed/link[@rel='first']"
    if (node is not None):
      testResults[testName] = "PASS"
    else:
      testResults[testName] = "FAIL"
    
    if node is not None:
      testName = "Found feed/link[@rel='first'][@href]"
      href = node.get("href")
      if (href is not None):
        testResults[testName] = "PASS"
    else:
      testResults[testName] = "FAIL"
    
    #### Parse the href URL and grab the startPage parameter to test for correct value
    
    # If startPage > 1, look for prev link
    if (int(startPage) > 1):
      node = root.find("./atom:link[@rel='prev']",namespaces=nsmap)
      testResults = {}
      testName = "Found feed/link[@rel='prev']"
      if (node is not None):
        testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
    
      if (node is not None):
        testName = "Found feed/link[@rel='prev'][@href]"
        href = node.get("href")
        if (href is not None):
          testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
        
        #### Parse the href URL and grab the startPage parameter to test for correct value
        
    else:
      node = root.find("./atom:link[@rel='prev']",namespaces=nsmap)
      testResults = {}
      testName = "Omit feed/link[@rel='prev'] on first page"
      if (node is not None):
        testResults[testName] = "FAIL"
      else:
        testResults[testName] = "PASS"
    
    # If startPage < number of pages, look for next link
    if (int(startPage) < numPages):
      node = root.find("./atom:link[@rel='next']",namespaces=nsmap)
      testResults = {}
      testName = "Found feed/link[@rel='next']"
      if (node is not None):
        testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
    
      if (node is not None):
        testName = "Found feed/link[@rel='next'][@href]"
        href = node.get("href")
        if (href is not None):
          testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
        
      #### Parse the href URL and grab the startPage parameter to test for correct value
          
    else:
      node = root.find("./atom:link[@rel='next']",namespaces=nsmap)
      testResults = {}
      testName = "Omit feed/link[@rel='next'] on last page"
      if (node is not None):
        testResults[testName] = "FAIL"
      else:
        testResults[testName] = "PASS"
    
    # Look for last link with correct number of pages
      node = root.find("./atom:link[@rel='last']",namespaces=nsmap)
      testResults = {}
      testName = "Found feed/link[@rel='last']"
      if (node is not None):
        testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
    
      if (node is not None):
        testName = "Found feed/link[@rel='last'][@href]"
        href = node.get("href")
        if (href is not None):
          testResults[testName] = "PASS"
      else:
        testResults[testName] = "FAIL"
        
      #### Parse the href URL and grab the startPage parameter to test for correct value
    
    return testResults
