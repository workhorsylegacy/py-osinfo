py-osinfo
=========

A module for getting the OS type, brand, release, and kernel with Python
2 & 3

Py-osinfo should work without any extra programs or libraries, beyond
what your OS provides. The goal is for this to work on every OS that
Python supports. Works on Linux, OS X, Windows, BSD, Solaris, Cygwin,
and Haiku.

Pip install
-----------

sudo pip install py-osinfo

sudo pip3 install py-osinfo

from osinfo import osinfo

Run as a script
---------------

::

    $ python osinfo.py
    type: Linux
    brand: Slackware
    release: 14.1
    kernel: (3, 13, 0)

Run as a library
----------------

::

    import osinfo
    os_type, os_brand, os_release, os_kernel = osinfo.get_os_info()

    if os_type in osinfo.OSType.linux:
        print("Looks like you're using Linux.")

        if os_kernel < (3, 13, 1):
            print("Your Linux kernel version is too old!")

    if os_brand in osinfo.OSBrand.CentOS:
        print("Looks like you're using CentOS.")

    if os_release == '99.01':
        print("OMG CentOS from 2099. Can I see the sorce code?")

Outputs
-------

**CentOS**

::

    type: Linux
    brand: CentOS
    release: 6.5
    kernel: (2, 6, 32)

**Cygwin**

::

    type: Cygwin
    brand: CYGWIN_NT-6.3
    release: 1.7.32
    kernel: (1, 7, 32)

**Crunch Bang**

::

    type: Linux
    brand: CrunchBang
    release: 11
    kernel: (3, 2, 0)

**Debian**

::

    type: Linux
    brand: Debian
    release: 7.6
    kernel: (3, 2, 0)

**Fedora 20**

::

    type: Linux
    brand: Fedora
    release: 20

**FreeBSD 10**

::

    type: BSD
    brand: FreeBSD
    release: 10.0

**Haiku**

::

    type: BeOS
    brand: Haiku
    release: 1
    kernel: (1,)

**Linux Mint**

::

    type: Linux
    brand: LinuxMint
    release: 10.9.4
    kernel: (3, 11, 10)

**Manjaro**

::

    type: Linux
    brand: Manjaro
    release: 0.8.10
    kernel: (3, 12, 20)

**Mac OS X**

::

    type: MacOS
    brand: OSX
    release: 10.9.4
    kernel: (13, 3, 0)

**NetBSD**

::

    type: BSD
    brand: NetBSD
    release: 6.1.4

**Open Indiana**

::

    type: Solaris
    brand: OpenIndiana
    release: 151a8
    kernel: (5, 11)

**open SUSE**

::

    type: Linux
    brand: openSUSE
    release: 13.1
    kernel: (3, 11, 10)

**Open SXCE**

::

    type: Solaris
    brand: OpenSXCE
    release: pensxce2014.05__illumos20140505
    kernel: (5, 11)

**PCBSD**

::

    type: BSD
    brand: FreeBSD
    release: 10.0-release-p13

**Redhat**

::

    type: Linux
    brand: Redhat
    release: 6.5
    kernel: (2, 6, 32)

**Sabayon**

::

    type: Linux
    brand: Sabayon
    release: 5.5
    kernel: (2, 6, 37)

**Scientific Linux**

::

    type: Linux
    brand: ScientificLinux
    release: 6.5
    kernel: (2, 6, 32)

**Ubuntu 14.04**

::

    type: Linux
    brand: Ubuntu
    release: 14.04
    kernel: (3, 13, 0)

**Windows 7**

::

    type: Windows
    brand: Windows7
    release: 6.1.7601
    kernel: (6, 1, 7601)

**Windows 8**

::

    type: Windows
    brand: Windows8
    release: 6.2.9200
    kernel: (6, 2, 9200)

**Windows XP**

::

    type: Windows
    brand: WindowsXP
    release: 5.1.2600
    kernel: (5, 1, 2600)

Please submit a pull request with the results for your favorite OS!

Bugs and Corrections
--------------------

Please report a Bug if you suspect any of this information is wrong.
