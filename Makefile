
all:
	@echo build: Builds the python source dist package
	@echo install: Installs python source dist package
	@echo clean: Removes any generated files

clean:
	rm -f -rf py_osinfo.egg-info
	rm -f -rf dist
	rm -f -rf py-osinfo-0.1.0
	rm -f -rf py-osinfo-0.1.0.tar.gz

build: clean
	python setup.py sdist
	mv dist/py-osinfo-0.1.0.tar.gz py-osinfo-0.1.0.tar.gz
	rm -f -rf py_osinfo.egg-info
	rm -f -rf dist

install: remove
	tar xzf py-osinfo-0.1.0.tar.gz
	cd py-osinfo-0.1.0/ && sudo python setup.py install
	rm -f -rf py-osinfo-0.1.0

	@echo now try "from osinfo import osinfo"
	@echo "osinfo.get_os_info()"

remove:
	sudo rm -f -rf /usr/local/lib/python2.7/dist-packages/py_osinfo-0.1.0-py2.7.egg



