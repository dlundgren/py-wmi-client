#!/usr/bin/env python

import os

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

from distutils.core import setup
import setuptools

setup(name='wmic',
      version='0.1.1',
      description='WMI client',
      license="MIT",
      author="David Lundgren",
      author_email="dlundgren@syberisle.net",
      include_package_data=True,
      install_requires=[
          'natsort',
          'pyasn1',
          'pycrypto',
          'impacket',
      ],
      scripts=[os.path.join('scripts', 'wmic')]
      )
