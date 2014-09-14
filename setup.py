# coding: utf-8

import io
import sys
from setuptools import setup, find_packages

from pathspec import __author__, __email__, __license__, __project__, __version__

# Read readme and changes files.
with io.open('README.rst', mode='r', encoding='UTF-8') as fh:
	readme = fh.read().strip()
with io.open('CHANGES.rst', mode='r', encoding='UTF-8') as fh:
	changes = fh.read().strip()

setup(
	name=__project__,
	version=__version__,
	author=__author__,
	author_email=__email__,
	url="https://github.com/cpburnz/python-path-specification",
	description="Utility library for gitignore style pattern matching of file paths.",
	long_description=readme + "\n\n" + changes,
	classifiers=[
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities",
	],
	license=__license__,
	packages=find_packages(),
	test_suite='pathspec.tests.test_gitignore.GitIgnoreTest',
	tests_require=['unittest2'] if sys.version_info < (2, 7) else [],
)
