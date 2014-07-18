py-osinfo
=========

Get the OS type, brand, and release with Python.

Py-osinfo should work without any extra programs or libraries, beyond 
what your OS provides. The goal is for this to work on every OS that Python 
supports.

Run as script
-----

    python osinfo.py
    # type: Linux
    # brand: Slackware
    # release: 14.1


Run as a library
-----

    import osinfo
    info = osinfo.get_os_info()
    print(info)
    # ('Linux', 'Slackware', '14.1')


Outputs
-----

__Ubuntu 14.04__

    type: Linux
    brand: Ubuntu
    release: 14.04

__FreeBSD 10__

    type: BSD
    brand: FreeBSD
    release: 10.0

Please submit a pull request with the results for your favorite OS!


Bugs and Corrections
-----

Please report a Bug if you suspect any of this information is wrong.

