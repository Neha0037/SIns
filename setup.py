# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in insurance_mgnt/__init__.py
from insurance_mgnt import __version__ as version

setup(
	name='insurance_mgnt',
	version=version,
	description='Insurance management',
	author='opetech',
	author_email='h@openetech',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
