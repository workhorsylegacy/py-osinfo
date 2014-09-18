
rm -f -rf py_osinfo.egg-info
rm -f -rf dist

python setup.py sdist
cd dist
tar xzf py-osinfo-0.1.0.tar.gz
cd py-osinfo-0.1.0/
sudo python setup.py install

# from osinfo import blah
# blah.go()
