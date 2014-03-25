import sys
import requests
from lxml import etree

# Print out the test results in a fixed format
def printResults(name,testResults):
    """ Print all of the test results passed in for the named site."""
    # Walk the testResults array and print the results for each test
    if testResults:
        for testName in testResults:
            print "*%s* %s: Test \'%s\'" % (testResults[testName],name,testName)
    else:
        print "*FAIL* %s: No test results found" % name


# Run this one time to parse the XML into an ElementTree
def runOnce(xmlResponse):
    """ Run one time at the start of the test.
        This parses the XML response into the tree object for later processing with lxml
        """
    # Check that we can parse the XML response string
    try:
        root = etree.fromstring(xmlResponse)
    except:
        print "*FAIL* Could not parse response"
        print "Got: "
        print xmlResponse
        print " "
        return
    return root


# Pretty-print out the returned response
def printResponse(root):
    # If we can parse it, try to print a nice version of it out
    try:
        print(etree.tostring(root, pretty_print="PASS"))
    except:
        print "*FAIL* Could not parse document to print"
        print " "
        return
    return root
