py-osinfo
=========

Get the OS type, brand, release, and kernel with Python.

Py-osinfo should work without any extra programs or libraries, beyond 
what your OS provides. The goal is for this to work on every OS that Python 
supports.

Run as a script
-----

    $ python osinfo.py
    type: Linux
    brand: Slackware
    release: 14.1
    kernel: (3, 13, 0)


Run as a library
-----

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
-----

__CentOS__

    type: Linux
    brand: CentOS
    release: 6.5
    kernel: (2, 6, 32)

__Cygwin__

    type: Cygwin
    brand: CYGWIN_NT-6.3
    release: 1.7.32
    kernel: (1, 7, 32)

__Crunch Bang__

    type: Linux
    brand: CrunchBang
    release: 11
    kernel: (3, 2, 0)

__Debian__

    type: Linux
    brand: Debian
    release: 7.6
    kernel: (3, 2, 0)

__Fedora 20__

    type: Linux
    brand: Fedora
    release: 20

__FreeBSD 10__

    type: BSD
    brand: FreeBSD
    release: 10.0

__Haiku__

    type: BeOS
    brand: Haiku
    release: 1
    kernel: (1,)

__Linux Mint__

    type: Linux
    brand: LinuxMint
    release: 10.9.4
    kernel: (3, 11, 10)

__Manjaro__

    type: Linux
    brand: Manjaro
    release: 0.8.10
    kernel: (3, 12, 20)

__Mac OS X__

    type: MacOS
    brand: OSX
    release: 10.9.4
    kernel: (13, 3, 0)

__NetBSD__

    type: BSD
    brand: NetBSD
    release: 6.1.4

__Open Indiana__

    type: Solaris
    brand: OpenIndiana
    release: 151a8
    kernel: (5, 11)

__open SUSE__

    type: Linux
    brand: openSUSE
    release: 13.1
    kernel: (3, 11, 10)

__PCBSD__

    type: BSD
    brand: FreeBSD
    release: 10.0-release-p13

__Redhat__

    type: Linux
    brand: Redhat
    release: 6.5
    kernel: (2, 6, 32)

__Sabayon__

    type: Linux
    brand: Sabayon
    release: 5.5
    kernel: (2, 6, 37)

__Scientific Linux__

    type: Linux
    brand: ScientificLinux
    release: 6.5
    kernel: (2, 6, 32)

__Ubuntu 14.04__

    type: Linux
    brand: Ubuntu
    release: 14.04
    kernel: (3, 13, 0)

__Windows 7__

    type: Windows
    brand: Windows7
    release: 6.1.7601
    kernel: (6, 1, 7601)

__Windows 8__

    type: Windows
    brand: Windows8
    release: 6.2.9200
    kernel: (6, 2, 9200)

__Windows XP__

    type: Windows
    brand: WindowsXP
    release: 5.1.2600
    kernel: (5, 1, 2600)


Please submit a pull request with the results for your favorite OS!


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

