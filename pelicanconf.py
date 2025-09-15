#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Thomas Brunbjerg'
SITENAME = 'Portfolio'
SITEURL = ''

THEME = "theme/mytheme"

PATH = 'content'

STATIC_PATHS = ['img', 'img/favicon.ico']

EXTRA_PATH_METADATA = {
    'img/favicon.ico': {'path': 'favicon.ico'},
}

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

#PLUGIN_PATHS = ["content/plugins", "plugins","./pelican-plugins"]
#PLUGINS = ["render_math"]

ARTICLE_PATHS = ['posts', 'articles']
ARTICLE_EXCLUDES = ['articles']

TAG_SAVE_AS = '{slug}.html'
TAG_URL = '{slug}.html'

GITHUB_URL = 'https://github.com/ThomB93'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
SUMMARY_MAX_LENGTH = 40

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

EXTRA_PATH_METADATA = {
    'img/favicon.ico': {'path': 'favicon.ico'}
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True