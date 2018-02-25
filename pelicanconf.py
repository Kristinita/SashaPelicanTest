# -*- coding: utf-8 -*-
# @Author: Kristinita
# @Date: 2017-01-17 17:43:09
# @Last Modified time: 2018-02-25 18:42:20

import logging
""" logging pelican module.

For disabling warnings:
http://docs.getpelican.com/en/stable/settings.html#logging
"""

import sys
"""sys module.

For download plugins from “plugins” folder.
"""

# That Pelican see plugins from this folder
sys.path.append('plugins')

# Do not touch in generation process

OUTPUT_RETENTION = [".git"]

GIT_SHA_METADATA = True

# ****************************************************************************
# *                                  General                                 *
# ****************************************************************************

AUTHOR = 'Саша Черных'
SITENAME = 'Поиск Кристиниты'
SITEURL = 'http://kristinita.ru'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'en'

# ****************************************************************************
# *                                   Feed                                   *
# ****************************************************************************

# Feed generation, perhaps, not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can edit those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


# ****************************************************************************
# *                                 Markdown                                 *
# ****************************************************************************

# Include Markdown extensions
# http://docs.getpelican.com/en/stable/settings.html?highlight=MARKDOWN#basic-settings
# https://pythonhosted.org/Markdown/extensions/#third-party-extensions

"""python markdown extensions.

Extensions, which Sasha's fan use.

#
# 1. extra
#

extra — set of extensions

Attribute List — add id and classes in Markdown
https://pythonhosted.org/Markdown/extensions/attr_list.html

Definition List — add dl, dd, dt tags
https://pythonhosted.org/Markdown/extensions/definition_lists.html
https://webref.ru/html/dd

Fenced code blocks — correct display multiline code blocks
https://pythonhosted.org/Markdown/extensions/fenced_code_blocks.html

Tables — simple tables
https://pythonhosted.org/Markdown/extensions/tables.html

#
# 2. Other default extensions
#

admonition — notes in Markdown
https://pythonhosted.org/Markdown/extensions/admonition.html

nl2br — new line without 2 br in line end
Like GitHub, not like Stack Overflow
https://pythonhosted.org/Markdown/extensions/nl2br.html

sane_lists — mix ordered/unordered list
https://pythonhosted.org/Markdown/extensions/sane_lists.html

#
# 3. facelessuser extensions
#

inlinehilite — inline highlight code
http://facelessuser.github.io/pymdown-extensions/extensions/inlinehilite/
https://pythonhosted.org/Markdown/extensions/code_hilite.html#step-2-add-css-classes

betterem — fix ** and __ symbols
http://facelessuser.github.io/pymdown-extensions/extensions/betterem/

"""

MARKDOWN = {
    'extension_configs': {
        # 'markdown.extensions.extra': {},
        # 'markdown.extensions.admonition': {},
        # 'markdown.extensions.nl2br': {},
        # 'markdown.extensions.sane_lists': {},
        # 'pymdownx.inlinehilite': {'css_class': 'SashaInlineHighlight',
        #                           'style_plain_text': True,
        #                           'use_codehilite_settings': False, },
        # 'pymdownx.betterem': {},
        # 'pymdownx.caret': {},
    },
    'output_format': 'html5',
}

# ****************************************************************************
# *                                Generation                                *
# ****************************************************************************

# Delete old site before building
DELETE_OUTPUT_DIRECTORY = False

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
    # 'filetime_from_git',
    # 'jinja2content',
    # 'pagefixer',
    # 'pelican_javascript',
    # 'interlinks',
    # 'section_number',
    # 'pelican-jinja2content',
    # 'photos'
]

JINJA2CONTENT_TEMPLATES = ['themes\sashapelican\templates']

PHOTO_ARTICLE = (760, 506, 80)

PHOTO_GALLERY = (1024, 768, 80)

PHOTO_LIBRARY = "pictures"

PHOTO_RESIZE_JOBS = -1

PHOTO_WATERMARK = True

PHOTO_WATERMARK_TEXT = SITENAME

PHOTO_THUMB = (192, 144, 60)

# Deadlinks
# https://github.com/silentlamb/pelican-deadlinks/tree/2689d7ebc4a3e05b74d681b46d9f6db7fd5f135e

DEADLINK_VALIDATION = True

DEADLINK_OPTS = {
    # Replace dead link to Internet Archive link
    'archive': True,
    'classes': ['SashaDeadlink'],
    # Disable «403» or «404» text after link in generated HTML
    'labels': False
}

# Sitemap
# https://github.com/getpelican/pelican-plugins/tree/master/sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0,
        'indexes': 0.5,
        'pages': 1
    },
    'changefreqs': {
        'articles': 'never',
        'indexes': 'weekly',
        'pages': 'always'
    }
}

# Section number
# https://github.com/getpelican/pelican-plugins/tree/master/section_number

SECTION_NUMBER_MAX = 5

# Interlinks for generate links for frequently used sites
# https://github.com/getpelican/pelican-plugins/tree/master/interlinks
INTERLINKS = {
    'kristinita': 'http://kristinita.ru/#gsc.tab=0&gsc.q='
}


# ****************************************************************************
# *                                   Paths                                  *
# ****************************************************************************

# Path for site content

PATH = 'content'

# Path for pages
# Don't set “PAGE_PATHS = ['']”! See
# https://github.com/getpelican/pelican/issues/2123

PAGE_PATHS = ['None']

# Path for articles
# [Hack] That exclude articles, include non-exicting folder.
# «ARTICLE_PATHS = None» — critical error, integer parameter

ARTICLE_PATHS = ['SashaTest']

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

# Typogrify library
# https://pypi.python.org/pypi/typogrify
# False, because bug with br in a newline:
# https://github.com/mintchaos/typogrify/pull/39
# Also unexpected &nbsp; after last word in line.

TYPOGRIFY = False

# Disable logging of empty alt attribute, needs “import logging” module

LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]
