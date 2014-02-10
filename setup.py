#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Daniel Rodriguez <danjrod@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

from setuptools import find_packages, setup

setup(
    name='TracChangelogFilter',
    version='0.0.1',
    packages=find_packages(),

    author='Daniel Rodriguez',
    author_email='danjrod@gmail.com',
    description="""A trac plugin that lets you filter changelog entries
        display based on defined rules (tbd)""",
    license="BSD 3-Clause",

    keywords='trac plugin security ticket comment group',
    url='http://trac-hacks.org/wiki/TracChangelogFilterPlugin',

    classifiers=['Framework :: Trac',],

    install_requires=['Trac'],

    entry_points={'trac.plugins': ['TracChangelogFilter = changelogfilter.changelogfilter',],},
)
