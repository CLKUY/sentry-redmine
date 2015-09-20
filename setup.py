#!/usr/bin/env python
"""
sentry-redmine
==================

An extension for Sentry which integrates with Redmine. Specifically, it allows you to easily create
Maniphest tasks from events within Sentry.

:copyright: (c) 2011 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
    'nose',
]

install_requires = [
    'sentry>=4.9.8',
    'requests>=0.2.0',
    'simplejson',
    'python-redmine'
]

setup(
    name='sentry-redmine',
    version='0.3.1',
    author='CLKUY',
    author_email='service@sentry.clk.com.uy',
    url='http://github.com/CLKUY/sentry-redmine',
    description='A Sentry extension which integrates with Redmine.',
    long_description=__doc__,
    license='BSD',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={
       'sentry.apps': [
            'redmine = sentry_redmine',
        ],
       'sentry.plugins': [
            'redmine = sentry_redmine.plugin:RedminePlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
