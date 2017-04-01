# -*- coding: utf-8 -*-

#  businessdate
#  ------------
#  A fast, efficient Python library for generating business dates inherited
#  from float for fast date operations. Typical banking business methods
#  are provided like business holidays adjustment, day count fractions.
#  Beside dates generic business periods offer to create time periods like
#  '10Y', '3 Months' or '2b'. Periods can easily added to business dates.
#
#  Author:  sonntagsgesicht <sonntagsgesicht@github.com>
#  Copyright: 2016, 2017 Deutsche Postbank AG
#  Website: https://github.com/sonntagsgesicht/businessdate
#  License: APACHE Version 2 License (see LICENSE file)


import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='businessdate',
    description='Python library for generating business dates for fast date operations and rich functionality.',
    version='0.2',
    author='Deutsche Postbank AG [sonntagsgesicht]',
    author_email='sonntagsgesicht@icloud.com',
    url='https://github.com/sonntagsgesicht/businessdate',
    bugtrack_url='https://github.com/sonntagsgesicht/businessdate/issues',
    license='Apache License 2.0',
    packages=['businessdate'],
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Office/Business :: Financial :: RiskManagement',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Utilities',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
    ],
)