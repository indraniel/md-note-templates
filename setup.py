#!/usr/bin/env python

import sys
from  setuptools import setup, find_packages
import os

def gather_requirements():
    requirements = []
    with open('./python/requirements.txt') as f:
        requirements = f.read().splitlines()

    github_string = '-e git+'

    (pkgs, deps) = ([], [])
    for r in requirements:
        pkg_name = r
        if r.startswith(github_string):
            url = r.replace(github_string, '')
            (url, egg) = url.split('#')
            pkg_name = url.split('/')[-1]
            tar = '/'.join([url, 'tarball/master#{}'.format(egg)])
            deps.append(tar)

        pkgs.append(pkg_name)

    return pkgs, deps

packages, dependencies = gather_requirements()

print 'Dependencies', "\n", dependencies
print 'Packages', "\n", packages
#sys.exit("Debug Exit")

version = '0.0.1'

setup(
    name='md-note-tools',
    version=version,
    install_requires=packages,
    dependency_links=dependencies,
    author='Indraniel',
    author_email='indraniel@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/indraniel/md-note-tools',
    license='BSD',
    description='R, Python, CSS and JavaScript templates used for rendering my markdown-based notes',
    entry_points={
        'console_scripts': [
            'gen-md = python.html:main',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
