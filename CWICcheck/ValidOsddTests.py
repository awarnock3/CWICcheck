from lxml import etree
from CwicCheckUtils import *

def testOsddElement(root):
    # Look for <feed> element to start
    if (root.tag == "{http://a9.com/-/spec/opensearch/1.1/}OpenSearchDescription"):
        return "PASS"
    return "FAIL"

def testShortNameElement(root):
    """ Test that the OSDD <ShortName> element is present and not empty
        """
    node = root.find("./opensearch:ShortName",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/ShortName"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <title> element is found, make sure it's not empty
        testName = "OpenSearchDescription/ShortName not empty"
        if node.text:
            testResults[testName] = "PASS"
        else: # <ShortName> element was empty
            testResults[testName] = "FAIL"
    else: # <ShortName> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testDescriptionElement(root):
    """ Test that the OSDD <Description> element is present and not empty
        """
    node = root.find("./opensearch:Description",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Description"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Description> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Description not empty"
        if node.text:
            testResults[testName] = "PASS"
        else: # <Description> element was empty
            testResults[testName] = "FAIL"
    else: # <Description> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testTagsElement(root):
    """ Test that the OSDD <Tags> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Tags",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Tags"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Tags> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Tags not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Tags> element isn't empty, check that we get the expected value
            testName = "Found Tags"
            if ("CWIC" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Tags>
                testResults[testName] = "FAIL"

        else: # <Tags> element was empty
            testResults[testName] = "FAIL"
    else: # <ShortName> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testContactElement(root):
    """ Test that the OSDD <Contact> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Contact",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Contact"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Contact> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Contact not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Contact> element isn't empty, check that we get the expected value
            testName = "Found Contact"
            if ("exec@wgiss.ceos.org" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Contact>
                testResults[testName] = "FAIL"

        else: # <Contact> element was empty
            testResults[testName] = "FAIL"
    else: # <Contact> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testImageElement(root):
    """ Test that the OSDD <Image> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Image",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Image"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Image> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Image not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Image> element isn't empty, check that we get the expected value
            testName = "Found Image"
            if ("favicon" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Image>
                testResults[testName] = "FAIL"

        else: # <Image> element was empty
            testResults[testName] = "FAIL"
    else: # <Image> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testDeveloperElement(root):
    """ Test that the OSDD <Developer> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Developer",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Developer"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Developer> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Developer not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Developer> element isn't empty, check that we get the expected value
            testName = "Found Developer"
            if ("CWIC Development Team" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Developer>
                testResults[testName] = "FAIL"

        else: # <Developer> element was empty
            testResults[testName] = "FAIL"
    else: # <Developer> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testAttributionElement(root):
    """ Test that the OSDD <Attribution> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Attribution",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Attribution"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Attribution> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Attribution not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Attribution> element isn't empty, check that we get the expected value
            testName = "Found Attribution"
            if ("NASA ECHO" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Attribution>
                testResults[testName] = "FAIL"

        else: # <Attribution> element was empty
            testResults[testName] = "FAIL"
    else: # <Attribution> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testSyndicationRightElement(root):
    """ Test that the OSDD <SyndicationRight> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:SyndicationRight",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/SyndicationRight"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <SyndicationRight> element is found, make sure it's not empty
        testName = "OpenSearchDescription/SyndicationRight not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <SyndicationRight> element isn't empty, check that we get the expected value
            testName = "Found SyndicationRight"
            if ("open" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <SyndicationRight>
                testResults[testName] = "FAIL"

        else: # <SyndicationRight> element was empty
            testResults[testName] = "FAIL"
    else: # <SyndicationRight> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testLanguageElement(root):
    """ Test that the OSDD <Language> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:Language",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Language"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Language> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Language not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <Language> element isn't empty, check that we get the expected value
            testName = "Found Language"
            if ("en-us" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <Language>
                testResults[testName] = "FAIL"

        else: # <Language> element was empty
            testResults[testName] = "FAIL"
    else: # <Language> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testOutputEncodingElement(root):
    """ Test that the OSDD <OutputEncoding> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:OutputEncoding",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/OutputEncoding"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Language> element is found, make sure it's not empty
        testName = "OpenSearchDescription/OutputEncoding not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <OutputEncoding> element isn't empty, check that we get the expected value
            testName = "Found OutputEncoding"
            if ("UTF-8" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <OutputEncoding>
                testResults[testName] = "FAIL"

        else: # <OutputEncoding> element was empty
            testResults[testName] = "FAIL"
    else: # <OutputEncoding> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testInputEncodingElement(root):
    """ Test that the OSDD <InputEncoding> element is present, not empty and
        contains the expected value of exec@wgiss.ceos.org
        """
    node = root.find("./opensearch:InputEncoding",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/InputEncoding"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <InputEncoding> element is found, make sure it's not empty
        testName = "OpenSearchDescription/InputEncoding not empty"
        if node.text:
            testResults[testName] = "PASS"            
            # Since the <InputEncoding> element isn't empty, check that we get the expected value
            testName = "Found InputEncoding"
            if ("UTF-8" in node.text):
                testResults[testName] = "PASS"
            else: # Got unexpected value for CWIC <InputEncoding>
                testResults[testName] = "FAIL"

        else: # <InputEncoding> element was empty
            testResults[testName] = "FAIL"
    else: # <InputEncoding> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testUrlElement(root):
    """ Test that the OSDD <Url> element is present and not empty
        """
    node = root.find("./opensearch:Url",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the element
    testName = "Found OpenSearchDescription/Url"
    if (node is not None):
        testResults[testName] = "PASS"

        # If the <Description> element is found, make sure it's not empty
        testName = "OpenSearchDescription/Url not empty"
        if node.text:
            testResults[testName] = "PASS"
        else: # <Url> element was empty
            testResults[testName] = "FAIL"
        
        testName = "Found OpenSearchDescription/Url[@type]"
        typeAttr = node.get("type")
        if (typeAttr is not None):
            testResults[testName] = "PASS"
            testName = "Found OpenSearchDescription/Url[@type] correct value"
            if ("application/atom+xml" in typeAttr):
                testResults[testName] = "PASS"
            else:
                testResults[testName] = "FAIL"
        else:
            testResults[testName] = "FAIL"

        testName = "Found OpenSearchDescription/Url[@template]"
        tmplAttr = node.get("template")
        if (tmplAttr is not None):
            testResults[testName] = "PASS"
            testName = "Found OpenSearchDescription/Url[@template] correct value"
            if ("http://cwictest.wgiss.ceos.org/opensearch/granules.atom" in tmplAttr):
                testResults[testName] = "PASS"
            else:
                testResults[testName] = "FAIL"
        else:
            testResults[testName] = "FAIL"
            
    else: # <Url> element was missing
        testResults[testName] = "FAIL"
    return testResults


def testUrlParameterElements(root):
    """ Test that the OSDD <params:Parameter> elements inside of <Url> are present and not empty
        """
    # Look for the parameter element for geoBox
    node = root.find("./opensearch:Url/params:Parameter[@name='geoBox']",namespaces=osdd_nsmap)
    testResults = {}
    
    # check that we can find the parameter element for geoBox
    testName = "Found OpenSearchDescription/Url/params:Parameter[@name='geoBox']"
    if (node is not None):
        testResults[testName] = "PASS"
        nodeValue = node.get("value")

        # If the <params:Parameter name='geoBox'> element is found, make sure it has the right attributes
        testName = "OpenSearchDescription/Url/params:Parameter[@name='geoBox'][@value] is correct"
        if ("geo:box" in nodeValue):
            testResults[testName] = "PASS"
        else: # <params:Parameter name='geoBox'> element was missing the value attribute
            testResults[testName] = "FAIL"
    else: # <params:Parameter name='geoBox'> element was missing
        testResults[testName] = "FAIL"
        

    # Look for the parameter element for timeStart
    node = root.find("./opensearch:Url/params:Parameter[@name='timeStart']",namespaces=osdd_nsmap)
    
    # check that we can find the parameter element for timeStart
    testName = "Found OpenSearchDescription/Url/params:Parameter[@name='timeStart']"
    if (node is not None):
        testResults[testName] = "PASS"
        nodeValue = node.get("value")

        # If the <params:Parameter name='timeStart'> element is found, make sure it has the right attributes
        testName = "OpenSearchDescription/Url/params:Parameter[@name='timeStart'][@value] is correct"
        if ("time:start" in nodeValue):
            testResults[testName] = "PASS"
        else: # <params:Parameter name='timeStart'> element was empty
            testResults[testName] = "FAIL"
    else: # <params:Parameter name='timeStart'> element was missing
        testResults[testName] = "FAIL"
        
    # Look for the parameter element for timeEnd
    node = root.find("./opensearch:Url/params:Parameter[@name='timeEnd']",namespaces=osdd_nsmap)
    
    # check that we can find the parameter element for timeEnd
    testName = "Found OpenSearchDescription/Url/params:Parameter[@name='timeEnd']"
    if (node is not None):
        testResults[testName] = "PASS"
        nodeValue = node.get("value")

        # If the <params:Parameter name='timeEnd'> element is found, make sure it has the right attributes
        testName = "OpenSearchDescription/Url/params:Parameter[@name='timeEnd'][@value] is correct"
        if ("time:end" in nodeValue):
            testResults[testName] = "PASS"
        else: # <params:Parameter name='timeEnd'> element was empty
            testResults[testName] = "FAIL"
    else: # <params:Parameter name='timeEnd'> element was missing
        testResults[testName] = "FAIL"
        
    # Look for the parameter element for startPage
    node = root.find("./opensearch:Url/params:Parameter[@name='startPage']",namespaces=osdd_nsmap)
    
    # check that we can find the parameter element for startPage
    testName = "Found OpenSearchDescription/Url/params:Parameter[@name='startPage']"
    if (node is not None):
        testResults[testName] = "PASS"
        nodeValue = node.get("value")

        # If the <params:Parameter name='startPage'> element is found, make sure it has the right attributes
        testName = "OpenSearchDescription/Url/params:Parameter[@name='startPage'][@value] is correct"
        if ("startPage" in nodeValue):
            testResults[testName] = "PASS"
        else: # <params:Parameter name='startPage'> element was empty
            testResults[testName] = "FAIL"
    else: # <params:Parameter name='startPage'> element was missing
        testResults[testName] = "FAIL"
        
    # Look for the parameter element for count
    node = root.find("./opensearch:Url/params:Parameter[@name='count']",namespaces=osdd_nsmap)
    
    # check that we can find the parameter element for startPage
    testName = "Found OpenSearchDescription/Url/params:Parameter[@name='count']"
    if (node is not None):
        testResults[testName] = "PASS"
        nodeValue = node.get("value")

        # If the <params:Parameter name='startPage'> element is found, make sure it has the right attributes
        testName = "OpenSearchDescription/Url/params:Parameter[@name='count'][@value] is correct"
        if ("count" in nodeValue):
            testResults[testName] = "PASS"
        else: # <params:Parameter name='count'> element was empty
            testResults[testName] = "FAIL"
    else: # <params:Parameter name='count'> element was missing
        testResults[testName] = "FAIL"
        
        
    return testResults

