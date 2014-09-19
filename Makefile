
VERSION = 0.2.0

all:
	@echo build: Builds the python source dist package
	@echo install: Installs python source dist package
	@echo clean: Removes any generated files
	@echo rst: uses pandoc to generate the README.rst file from README.md

clean:
	rm -f -rf py_osinfo.egg-info
	rm -f -rf dist
	rm -f -rf py-osinfo-$(VERSION)
	rm -f -rf py-osinfo-$(VERSION).tar.gz

build: clean
	python setup.py sdist
	mv dist/py-osinfo-$(VERSION).tar.gz py-osinfo-$(VERSION).tar.gz
	rm -f -rf py_osinfo.egg-info
	rm -f -rf dist

install: remove
	tar xzf py-osinfo-$(VERSION).tar.gz
	cd py-osinfo-$(VERSION)/ && sudo python setup.py install
	rm -f -rf py-osinfo-$(VERSION)

	@echo now try "from osinfo import osinfo"
	@echo "osinfo.get_os_info()"

remove:
	sudo rm -f -rf /usr/local/lib/python2.7/dist-packages/py_osinfo-$(VERSION)-py2.7.egg

rst:
	rm -f -rf README.rst
	pandoc --from=markdown --to=rst --output=README.rst README.md



