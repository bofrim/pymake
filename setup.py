from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))
_pkg_name = "pymake"
_read_me = "README"
_version = "0.0.1"

if sys.version_info[0] < 3:
    with open(os.path.join(_here, _read_me)) as readme:
        long_description = readme.read()
else:
    with open(os.path.join(_here, _read_me), encoding="utf-8") as readme:
        long_description = readme.read()


setup(
    name=_pkg_name,
    version=_version,
    description=("My fork of the Mozilla pymake project."),
    long_description=long_description,
    author="Brad Ofrim",
    author_email="bofrim@gmail.com",
    url="https://github.com/bofrim/pymake",
    packages=[_pkg_name],
    include_package_data=True,
)
