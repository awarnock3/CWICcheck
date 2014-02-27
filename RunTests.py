import sys, getopt
from CWICcheck.OpenSearch import openSearchTests

urls = {'INPE':       'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=5&clientId=CWICcheck',
        'USGS/LSI':   'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'GHRSST':     'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'NASA/ECHO':  'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=GES_DISC_TRMM_G2A12_V6&startPage=1&count=5&timeStart=1997-12-07T00:00:00Z&timeEnd=1997-12-14T00:00:00Z&geoBox=-180,-38,180,38&clientId=CWICcheck',
        'NASA/ECHO2': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&timeStart=2000-02-24T00:00:00Z&timeEnd=2014-02-19T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        }
usage = '[-n|--name <site name> -u|--url <site URL>]'

def main(argv):
    if not argv: # Nothing on the command line, so just run the defaults
        print "Running default tests"
        for key,value in urls.iteritems():
            openSearchTests(key,value)
        sys.exit()

    # Parse the command line
    try:
        opts, args = getopt.getopt(argv,"hn:u:",["name=","url="])
    except getopt.GetoptError: # Got something unrecognized, so bail out
            print 'RunTests.py %s' % usage
            sys.exit(2)

    # Grab the site name and URL from the command line and run the tests on that
    siteName = ''
    siteUrl  = ''
    for opt, arg in opts:
        if opt == '-h':
            print 'RunTests.py %s' % usage
            sys.exit()
        elif opt in ("-n", "--name"):
            siteName = arg
        elif opt in ("-u", "--url"):
            siteUrl = arg
    openSearchTests(siteName, siteUrl)
    print "Done."

# Default function
if __name__ == "__main__":
     main(sys.argv[1:])