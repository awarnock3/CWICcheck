import sys, getopt
from CWICcheck.OpenSearch import openSearchTests

urls = {'INPE5 first page':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE6 page 2':               'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=2&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE7 last page':            'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=3&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE2 default page & count': 'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE3 no times':             'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'INPE1 dataset only':         'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM',
        'INPE4 no spatial':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=INPE_LANDSAT7_ETM&startPage=1&count=3&timeStart=2008-02-04T00:00:00Z&timeEnd=2010-05-31T00:00:00Z&clientId=CWICcheck',

        'USGS/LSI1 dataset only':         'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8',
        'USGS/LSI2 default page & count': 'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'USGS/LSI3 no times':             'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'USGS/LSI4 no spatial':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&clientId=CWICcheck',
        'USGS/LSI5 first page':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=1&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'USGS/LSI6 page 2':               'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=2&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',
        'USGS/LSI7 last page':            'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=Landsat_8&startPage=16&count=5&timeStart=2013-06-01T00:00:00Z&timeEnd=2013-06-01T23:59:59Z&geoBox=-82.71,-18,82.74,18&clientId=CWICcheck',

        'GHRSST1 dataset only':         'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19',
        'GHRSST2 default page & count': 'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'GHRSST3 no times':             'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&geoBox=-76,24,73,78&clientId=CWICcheck',
        'GHRSST4 no spatial':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&clientId=CWICcheck',
        'GHRSST5 first page':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=1&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'GHRSST6 page 2':               'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=2&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',
        'GHRSST7 last page':            'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=EUR-L3P-NAR_AVHRR_NOAA_19&startPage=11&count=5&timeStart=2009-09-01T00:00:00Z&timeEnd=2009-09-02T00:00:00Z&geoBox=-76,24,73,78&clientId=CWICcheck',

        'NASA/ECHO1 dataset only':         'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5',
        'NASA/ECHO2 default page & count': 'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-02-28T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'NASA/ECHO3 no times':             'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&startPage=1&count=2&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'NASA/ECHO4 no spatial':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&startPage=1&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-02-28T00:00:00Z&clientId=CWICcheck',
        'NASA/ECHO5 first page':           'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&startPage=1&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-02-28T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'NASA/ECHO6 page 2':               'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&startPage=2&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-02-28T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',
        'NASA/ECHO7 last page':            'http://cwic.wgiss.ceos.org/opensearch/granules.atom?datasetId=MOD10C2V5&startPage=5&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-02-28T00:00:00Z&geoBox=-180,-90,180,90&clientId=CWICcheck',

        'CCMEO1 full': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=CWIC_REG&startPage=1&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-01-02T00:00:00Z&geoBox=-140,45,-130,90&clientId=CWICcheck',
        'CCMEO2 default page & count': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=CWIC_REG&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-01-02T00:00:00Z&geoBox=-140,45,-130,90&clientId=CWICcheck',
        'CCMEO1 first page': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=CWIC_REG&startPage=1&count=3&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-01-02T00:00:00Z&geoBox=-140,45,-130,90&clientId=CWICcheck',
        'CCMEO1 page 2': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=CWIC_REG&startPage=2&count=2&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-01-02T00:00:00Z&geoBox=-140,45,-130,90&clientId=CWICcheck',
        'CCMEO1 last page': 'http://cwictest.wgiss.ceos.org/opensearch/granules.atom?datasetId=CWIC_REG&startPage=3&count=3&timeStart=2014-01-01T00:00:00Z&timeEnd=2014-01-02T00:00:00Z&geoBox=-140,45,-130,90&clientId=CWICcheck',

        'FedEO dc:subject, geo:box': "http://geo.spacebel.be/opensearch/request/?httpAccept=application/atom%2Bxml&subject=MYD10A2V5&startRecord=1&maximumRecords=10&bbox=-74,17,-67,20.5",
        }
usage = """[-u|--url <site URL> -v|--verbose <level>]
        -v full     Show all output (default)
        -v headers  Show HTTP response header only
        -v response Show XML response only
        -v feed     Run tests on <feed> elements response only
        -v paging   Run tests on paging hyperlinks in <feed> only
        -v entry    Run tests on <entry> elements only
        """

def main(argv):
    """ Run all of the tests against either the default list of sites or with the site given on the command line."""

    # Grab the test name and URL from the command line and run the tests on that
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
            elif opt in ("-u", "--url"):
                siteName = "Command Line"
                siteUrl = arg
            elif opt in ("-v", "--verbose"):
                verbose = arg
                
    # Run one test if URL given on command line.  Otherwise, run the defaults
    if siteUrl:
        openSearchTests(siteName, siteUrl,verbose)
    else: # or just run the defaults
        print "Running default tests"
        for key,value in sorted(urls.items()):
            openSearchTests(key,value,verbose)
            print " "
        print "Done."
        sys.exit()

    print "Done."

# Set up the default function
if __name__ == "__main__":
     main(sys.argv[1:]) 