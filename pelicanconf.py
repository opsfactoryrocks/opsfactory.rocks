#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'opsfactory'
SITENAME = u'opsfactory'
SITEURL = 'https://opsfactoryrocks.github.io/opsfactory.rocks'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
OUTPUT_PATH = 'docs/'

THEME = 'themes/martin-pelican'
SUMMARY_MAX_LENGTH = None

SITESUBTITLE = u'devops made simple'
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Home', '/'), ('Blog', '/blog.html')]
# Add header background image from content/images : 'background.jpg'

# Static files
#STATIC_PATHS = ['extra/CNAME']
#EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
INDEX_SAVE_AS = 'blog.html'
