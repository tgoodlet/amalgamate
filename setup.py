#! /usr/bin/env python
import sys
try:
    from setuptools import setup
    HAVE_SETUPTOOLS = True
except ImportError:
    from distutils.core import setup
    HAVE_SETUPTOOLS = False


VERSION = "0.1.0"

setup_kwargs = {
    "version": VERSION,
    "description": 'Collapses Python packages into a single module.',
    "author": 'The xonsh developers',
    "author_email": 'xonsh@googlegroups.com',
    "url": 'https://github.com/xonsh/amalgamate',
    "download_url": "https://github.com/scopatz/xo/zipball/" + VERSION,
    "classifiers": [
        "License :: OSI Approved",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Utilities",
        ],
    "zip_safe": False,
    "data_files": [("", ['LICENSE', 'README.rst']),],
    }


if __name__ == '__main__':
    setup(
        name='exofrills',
        py_modules=['amalgamate'],
        entry_points={'console_scripts': ['xo = xo:main',],},
        long_description=open('README.rst').read(),
        **setup_kwargs
        )
