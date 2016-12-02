#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'wheel',
    'click',
    'matplotlib',
    'numpy',
    'requests',
    'pillow',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pydisp',
    version='0.0.1',
    description="python client for display",
    # long_description=readme + '\n\n' + history,
    long_description=readme + '\n',
    author="Daniel Maturana",
    author_email='dimatura@cmu.edu',
    url='https://github.com/dimatura/pydisp',
    packages=[
        'pydisp',
    ],
    scripts=[
        'scripts/disp',
    ],
    package_dir={'pydisp':
                 'pydisp'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pydisp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
