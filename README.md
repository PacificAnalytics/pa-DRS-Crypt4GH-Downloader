[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://mit-license.org/)
![Travis (.org)](https://img.shields.io/travis/ga4gh/ga4gh-drs-client?style=flat-square)
[![Read the Docs](https://img.shields.io/readthedocs/ga4gh-drs-client.svg?style=flat-square)](https://ga4gh-drs-client.readthedocs.io/en/latest/)
![Coveralls github](https://img.shields.io/coveralls/github/ga4gh/ga4gh-drs-client?style=flat-square)
![PyPI](https://img.shields.io/pypi/v/ga4gh-drs-client?style=flat-square)
[![Python 3.6](https://img.shields.io/badge/python-3.6%20|%203.7-blue.svg?style=flat-square)](https://www.python.org)

# ga4gh-drs-client

The GA4GH DRS Client is a Python-based command-line application for requesting
omics data and metadata from web services that are compliant with the [Data Repository Service (DRS) API Specification](https://github.com/ga4gh/data-repository-service-schemas). The DRS API specification, developed
by the [Global Alliance for Genomics and Health](https://www.ga4gh.org/), serves to provide a standardized
API framework to allow for interoperability of datasets hosted at different
institutions.

## PA-specific changes

The following changes were made to the DRS client to support the DRS-Crypt4GH usecase:

1. Temporarily allow HTTP (GH [#1](https://github.com/PacificAnalytics/pa-DRS-Crypt4GH-Downloader/pull/1)). Allows for downloading from resources that support only HTTP.
2. Pass in Crypt4GH key (GH [#2](https://github.com/PacificAnalytics/pa-DRS-Crypt4GH-Downloader/pull/2)). Allows for passing in a Crypt4GH public key as an HTTP header. To pass in a key, set the `CRYPT4GH_PUBKEY` environment variable.

## Installation and Usage

Please review the [GA4GH DRS Client Documentation](https://ga4gh-drs-client.readthedocs.io/en/latest/) for instructions on how to install and use the command-line application.

## Additional Resources

1. [PyPI](https://pypi.org/project/ga4gh-drs-client/) - The DRS Client is 
available on the Python Package Index (PyPI)
2. [Docker](https://hub.docker.com/r/ga4gh/ga4gh-drs-client) - The DRS Client
can be run through a preconfigured image
