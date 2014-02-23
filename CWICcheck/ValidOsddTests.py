from lxml import etree

def isOsddResponse(response):
  root = etree.fromstring(response)
  # Look for <feed> element to start
  print root.tag
  if (root.tag == "OpenSearchDescription"):
    return true
  return false
