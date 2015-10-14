#!/usr/bin/env python

import os

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'): os.remove('MANIFEST')

from distutils.core import setup

setup(name='wmic',
      version='0.1',
      description='WMI client',
      packages=['wmic'],
      include_package_data=True,
      install_requires=[
          'pyasn1',
          'pycrypto',
          'impacket',
          'natsort'
      ],
      scripts=[os.path.join('scripts', 'wmic')]
      )
