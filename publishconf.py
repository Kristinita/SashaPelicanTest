#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file used if use `make publish` or
# explicitly specify it as your config file.

import os
import sys

import pelicanconf  # NOQA
"""pelicanconf module.

Import settings from pelicanconf.py file.
Ignore flake8 errors/warnings in this line:
http://stackoverflow.com/a/10506715/5951529
"""

sys.path.append(os.curdir)

# Absolute path, if site publish
# Don't use relative paths for publishing!
# SITEURL = 'http://kristinita.ru'
RELATIVE_URLS = True

PLUGINS = [
    'pagefixer',
    'pelican_javascript',
    'sitemap', 'interlinks',
    'section_number',
    'optimize_images', 'deadlinks']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
