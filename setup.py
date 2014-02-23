try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A set of testing scripts to massage the CWIC OpenSearch interface',
    'author': 'Archie Warnock',
    'download_url': 'http://www.awcubed.com',
    'author_email': 'warnock@awcubed.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CWICcheck', 'requests', 'lxml', 'urlparse'],
    'scripts': [],
    'name': 'CWICcheck'
}

setup(**config)