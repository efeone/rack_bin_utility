from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rack_bin_utility/__init__.py
from rack_bin_utility import __version__ as version

setup(
	name="rack_bin_utility",
	version=version,
	description="Frappe application to maintain Products or any  other related things in an ordered maner",
	author="efeone",
	author_email="info@efeone.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
