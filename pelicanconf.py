#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'grouptwo'
SITENAME = 'TCMG412_Grouptwo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Dev Team:', 'http://getpelican.com/'),
         ('Emily D.', 'http://python.org/'),
         ('Brandon K.', 'http://jinja.pocoo.org/'),
         ('Robert W.', '#'),
         ('Ops Team:', '#'),
        ('Michael M.', '#'),
        ('Emily P.', '#'),
        ('Matt S.', '#'),
         )

THEME = '/home/emilydinh/pelican-themes/pelican-bootstrap3'
PLUGIN_PATHS = ['/home/emilydinh/grouptwo/pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
            }


# Social widget

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
