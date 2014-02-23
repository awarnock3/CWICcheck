try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Describe the project here',
    'author': 'Archie Warnock',
    'download_url': 'http://www.awcubed.com',
    'author_email': 'warnock@awcubed.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CWICcheck'],
    'scripts': [],
    'name': 'CWICcheck'
}

setup(**config)