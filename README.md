py-osinfo
=========

Get the OS type, brand, and release with Python.

Py-osinfo should work without any extra programs or libraries, beyond 
what your OS provides. The goal is for this to work on every OS that Python 
supports.

Run as a script
-----

    $ python osinfo.py
    type: Linux
    brand: Slackware
    release: 14.1


Run as a library
-----

    import osinfo
    os_type, os_brand, os_release = osinfo.get_os_info()

    if os_type in osinfo.OSType.linux:
        print("Looks like you're using Linux.")

    if os_brand in osinfo.OSBrand.CentOS:
        print("Looks like you're using CentOS.")

    if os_release == '99.01':
        print("OMG CentOS from 2099. Can I see the sorce code?")


Outputs
-----

__CentOS__

    type: Linux
    brand: CentOS
    release: 6.5

__Crunch Bang__

    type: Linux
    brand: CrunchBang
    release: 11

__Debian__

    type: Linux
    brand: Debian
    release: 7.6

__Fedora 20__

    type: Linux
    brand: Fedora
    release: 20	

__FreeBSD 10__

    type: BSD
    brand: FreeBSD
    release: 10.0

__Linux Mint__

    type: Linux
    brand: LinuxMint
    release: 10.9.4

__Mac OS X__

    type: MacOS
    brand: OSX
    release: 10.9.4

__Open Indiana__

    type: Solaris
    brand: OpenIndiana
    release: 151a3

__open SUSE__

    type: Linux
    brand: openSUSE
    release: 13.1

__Sabayon__

    type: Linux
    brand: Sabayon
    release: 5.5

__Ubuntu 14.04__

    type: Linux
    brand: Ubuntu
    release: 14.04

__Windows 7__

    type: Windows
    brand: Windows7
    release: 6.1.7601

__Windows 8__

    type: Windows
    brand: Windows8
    release: 6.2.9200

__Windows XP__

    type: Windows
    brand: WindowsXP
    release: 5.1.2600


Please submit a pull request with the results for your favorite OS!


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

