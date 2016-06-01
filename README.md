Python WMI Client
=================

[![Current version on PyPI](http://img.shields.io/pypi/v/wmic.svg)][pypi]
[![Downloads/month on PyPI](http://img.shields.io/pypi/dm/wmic.svg)][pypi]

Communicate with Windows machines via WMI from *nix machines.

Motivation
----------

The original wmic was/is a command-line utility originally built as part of Samba. It has become difficult to find the
correct requirements for building it manually, and there were to my knowledge no available packages for the differing
platforms that I use.

While the current implementation aims to be compatible with [check_wmi_plus.pl](http://www.edcint.co.nz/checkwmiplus/), getting feature parity with the
original/compiled version of wmic is not out of the question.

Installation
------------

To install simply run the following:

```bash
$ pip install wmic
```

##### Requirements

* impacket >= 0.9.13
* natsort >= 3

Usage
-----

The simplest way to run it is similar to the following

```wmic -A /etc/nagios3/wmic_auth.ini //ServerName "SELECT * FROM Win32_PerfFormattedData_PerfOS_Memory"```

##### Available arguments

* ```-A```, ```--authentication-file``` : INI style file that
    * ```domain``` : optional, default: WORKGROUP
    * ```username``` : required
    * ```password``` : required
* ```-U```,```--user``` : format ```[DOMAIN\]USERNAME[%PASSWORD]```
* ```--delimiter``` : how to separate the colums, default: |
* ```--namespace``` : namespace, default: //./root/cimv2

##### Notes

* If you do not supply a domain, then the script defaults to ```WORKGROUP```
* You must use either a file or user argument

License
-------

MIT
