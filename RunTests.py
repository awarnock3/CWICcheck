import sys, getopt
from CWICcheck.OpenSearch import openSearchTests

urls = {'INPE first page':           'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE page 2':               'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=2&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE last page':            'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=3&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE default page & count': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE no times':             'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE dataset only':         'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM',
        'INPE no spatial':           'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&clientId=CWICcheck',

        'USGS/LSI':   'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
#        'GHRSST':     'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
#        'NASA/ECHO':  'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=GES_DISC_TRMM_G2A12_V6&startPage=1&count=5&timeStart=1997-12-07T00:00:00Z&timeEnd=1997-12-14T00:00:00Z&geoBox=-180,-38,180,38&clientId=CWICcheck',
#        'NASA/ECHO2': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&timeStart=2000-02-24T00:00:00Z&timeEnd=2014-02-19T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        }
usage = """[-n|--name <site name> -u|--url <site URL> -v|--verbose <level>]
        -v full     Show all output (default)
        -v headers  Show HTTP response header only
        -v response Show XML response only
        -v feed     Run tests on <feed> elements response only
        -v paging   Run tests on paging hyperlinks in <feed> only
        -v entry    Run tests on <entry> elements only
        """

def main(argv):
    """ Run all of the tests against either the default list of sites or with the site given on the command line."""

    # Grab the site name and URL from the command line and run the tests on that
    siteName = None
    siteUrl  = None
    verbose  = "full"

    if argv: # If something is on the command line
        # Parse the command line
        try:
            opts, args = getopt.getopt(argv,"hn:u:v:",["name=","url=","verbose="])
        except getopt.GetoptError: # Got something unrecognized, so bail out
            print 'RunTests.py %s' % usage
            sys.exit(2)
        # Grab any options that are there
        for opt, arg in opts:
            if opt == '-h':
                print 'RunTests.py %s' % usage
                sys.exit()
            elif opt in ("-n", "--name"):
                siteName = arg
            elif opt in ("-u", "--url"):
                siteUrl = arg
            elif opt in ("-v", "--verbose"):
                verbose = arg
                
    # Run one test if URL given on command line.  Otherwise, run the defaults
    if siteUrl:
        openSearchTests(siteName, siteUrl,verbose)
    else: # or just run the defaults
        print "Running default tests"
        for key,value in urls.iteritems():
            openSearchTests(key,value,verbose)
            print " "
        print "Done."
        sys.exit()

    print "Done."

# Set up the default function
if __name__ == "__main__":
     main(sys.argv[1:])