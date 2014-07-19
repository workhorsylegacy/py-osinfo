#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Copyright (c) 2014, Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
# Py-osinfo is a Python module to get the OS type, brand, and release
# It uses a MIT style license
# It is hosted at: https://github.com/workhorsy/py-osinfo
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import platform


class OSType(object):
	bsd = ['BSD']
	cygwin = ['Cygwin']
	darwin = ['Darwin']
	linux = ['Linux']
	solaris = ['Solaris']
	windows = ['Windows']

	unknown = ['Unknown']

	withoutRoot = [windows, cygwin]
	unix = [bsd, darwin, solaris]
	nix = [bsd, darwin, linux, solaris]

class OSBrand(object):
	Arch = ['Arch']
	ArchBang = ['ArchBang']
	BeOS = ['BeOS']
	Bodhi = ['Bodhi']
	CentOS = ['CentOS']
	Chakra = ['Chakra']
	Clonezilla = ['Clonezilla']
	CrunchBang = ['CrunchBang']
	DamnSmallLinux = ['DamnSmallLinux']
	Debian = ['Debian']
	DragonFlyBSD = ['DragonFlyBSD']
	elementary = ['elementary']
	Fedora = ['Fedora']
	FreeBSD = ['FreeBSD']
	Gentoo = ['Gentoo']
	GoboLinux = ['GoboLinux']
	Haiku = ['Haiku']
	Kali = ['Kali']
	KNOPPIX = ['KNOPPIX']
	Kubuntu = ['Kubuntu']
	Lubuntu = ['Lubuntu']
	LXLE = ['LXLE']
	MacOS = ['MacOS']
	Mageia = ['Mageia']
	Manjaro = ['Manjaro']
	MEPIS = ['MEPIS']
	Mint = ['Mint']
	NetBSD = ['NetBSD']
	OpenBSD = ['OpenBSD']
	OpenIndiana = ['OpenIndiana']
	OpenSolaris = ['OpenSolaris']
	openSUSE = ['openSUSE']
	OracleLinux = ['OracleLinux']
	OSX = ['OSX']
	Parsix = ['Parsix']
	PeppermintOS = ['PeppermintOS']
	PCBSD = ['PCBSD']
	PCLinuxOS = ['PCLinuxOS']
	Puppy = ['Puppy']
	Redhat = ['Redhat']
	Sabayon = ['Sabayon']
	Salix = ['Salix']
	Siduction = ['Siduction']
	ScientificLinux = ['ScientificLinux']
	Simplicity = ['Simplicity']
	Slackware = ['Slackware']
	Sparky = ['Sparky']
	Solaris = ['Solaris']
	SteamOS = ['SteamOS']
	Tanglu = ['Tanglu']
	Trisquel = ['Trisquel']
	Ubuntu = ['Ubuntu']
	UbuntuStudio = ['UbuntuStudio']
	UltimateEdition = ['UltimateEdition']
	Vector = ['Vector']
	WindowsXP = ['WindowsXP']
	WindowsVista = ['WindowsVista']
	Windows7 = ['Windows7']
	Windows8 = ['Windows8']
	Xubuntu = ['Xubuntu']
	Zorin = ['Zorin']

	unknown = ['Unknown']

def _get_os_type():
	os_type = OSType.unknown[0]

	# Figure out the general OS type
	uname = platform.system().lower()
	if 'bsd' in uname:
		os_type = OSType.bsd[0]
	elif 'cygwin' in uname:
		os_type = OSType.cygwin[0]
	elif 'darwin' in uname:
		os_type = OSType.darwin[0]
	elif 'linux' in uname:
		os_type = OSType.linux[0]
	elif 'solaris' in uname or 'sunos' in uname:
		os_type = OSType.solaris[0]
	elif 'windows' in uname:
		os_type = OSType.windows[0]

	return os_type

def _get_os_brand(os_type):
	dist = platform.dist()

	# Figure out the brand
	if os_type in OSType.linux:
		linux_dist = platform.linux_distribution()
		name = linux_dist[0].lower() or dist[0].lower()

		if name in 'centos':
			return OSBrand.CentOS[0]
		elif name in 'ubuntu':
			return OSBrand.Ubuntu[0]
	elif os_type in OSType.bsd:
		name = dist[0].lower() or platform.system().lower()

		if name in 'dragonflybsd':
			return OSBrand.DragonFlyBSD[0]
		elif name in 'freebsd':
			return OSBrand.FreeBSD[0]
		elif name in 'netbsd':
			return OSBrand.NetBSD[0]
		elif name in 'openbsd':
			return OSBrand.OpenBSD[0]
		elif name in 'pcbsd':
			return OSBrand.PCBSD[0]
	elif os_type in OSType.darwin:
		name = platform.mac_ver()[0].lower()
		if name.startswith('10'):
			return OSBrand.OSX
	elif os_type in OSType.solaris:
		ver = platform.version().lower()
		if ver.startswith('oi_'):
			return OSBrand.OpenIndiana
	elif os_type in OSType.windows:
		name = platform.release().lower()

		if name in 'xp':
			return OSBrand.WindowsXP[0]
		elif name in 'vista':
			return OSBrand.WindowsVista[0]
		elif name in '7':
			return OSBrand.Windows7[0]
		elif name in '8':
			return OSBrand.Windows8[0]

	return OSBrand.unknown[0]

def _get_os_release(os_type):
	os_release = 'unknown'
	dist = platform.dist()

	# Figure out the release
	if os_type in OSType.bsd:
		os_release = platform.release().lower().rstrip('-release')
	elif os_type in OSType.linux:
		linux_dist = platform.linux_distribution()
		os_release = linux_dist[1].lower() or dist[1].lower()
	elif os_type in OSType.darwin:
		os_release = platform.mac_ver()[0].lower()
		#print(platform.release()) # Kernel version: 13.3.0
	elif os_type in OSType.solaris:
		ver = platform.version().lower()
		os_release = ver.lstrip('oi_')
	elif os_type in OSType.windows:
		dist = platform.version().lower()
		os_release = dist

	#cygwin = ['Cygwin']

	return os_release

def get_os_info():
	os_type = _get_os_type()
	os_brand = _get_os_brand(os_type)
	os_release = _get_os_release(os_type)

	return (os_type, os_brand, os_release)

if __name__ == '__main__':
	info = get_os_info()
	print('type: {0}'.format(info[0]))
	print('brand: {0}'.format(info[1]))
	print('release: {0}'.format(info[2]))




