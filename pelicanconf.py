#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
"""sys module.

For download plugins from “plugins” folder.
"""

# That Pelican see plugins from this folder
sys.path.append('plugins')

# ****************************************************************************
# *                                  General                                 *
# ****************************************************************************

AUTHOR = 'Саша Черных'
SITENAME = 'Поиск Кристиниты'
SITEURL = 'http://kristinita.ru'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'en'


# ****************************************************************************
# *                                 Markdown                                 *
# ****************************************************************************

# Include Markdown extensions
# http://docs.getpelican.com/en/stable/settings.html?highlight=MARKDOWN#basic-settings
# https://pythonhosted.org/Markdown/extensions/#third-party-extensions
MARKDOWN = {
    'extension_configs': {
        # Fenced code blocks
        # Correct displaying code blocks
        # https://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html
        'markdown.extensions.extra': {},
        # Admonition
        # Notes rendering
        # https://pythonhosted.org/Markdown/extensions/admonition.html
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

# ****************************************************************************
# *                                Generation                                *
# ****************************************************************************

# Delete old site before building
DELETE_OUTPUT_DIRECTORY = True

# Do not touch in generation process
OUTPUT_RETENTION = [".git"]

LOAD_CONTENT_CACHE = False

# Relative URLs for developing
RELATIVE_URLS = True

# Original format without rendering. If true, md rendering to md,
# not md → html
OUTPUT_SOURCES = False

# ****************************************************************************
# *                                  Plugins                                 *
# ****************************************************************************

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    'pagefixer',
    'pelican_javascript',
    'interlinks',
    'section_number',
]

# ****************************************************************************
# *                                   Paths                                  *
# ****************************************************************************

# Path for site content

PATH = 'content'

# Path for pages
# Don't set “PAGE_PATHS = ['']”! See
# https://github.com/getpelican/pelican/issues/2123

PAGE_PATHS = ['Gingerinas', 'Giologica', 'Life-hacks', 'Sasha-Black',
              'Smert-svobode', 'Sublime-Text']

# Path for articles
# [Hack] That exclude articles, include non-exicting folder.
# «ARTICLE_PATHS = None» — critical error, integer parameter

ARTICLE_PATHS = ['None']

# Non-modified files and folders
# [Hack] The register matters. 404.md & 404.html don't work.

STATIC_PATHS = ['']

# That filename = Slug, not necessary to write slug manually for each article

SLUGIFY_SOURCE = 'basename'

# Extra path metadata
# http://manos.im/blog/static-site-pelican-grunt-travis-github-pages/

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = CATEGORY_URL
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tag/alltags.html'

# ****************************************************************************
# *                                   Other                                  *
# ****************************************************************************

# Theme

THEME = 'themes/sashapelican'

# Pagination — division of articles

DEFAULT_PAGINATION = False
