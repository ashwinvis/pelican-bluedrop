#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = "Blue Drop"
SITENAME = "Blue Drop's Website"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Stockholm"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "bluedrop"

# Backdrop specific variables
SITESUBTITLE = ""
SITE_DESCRIPTION = "I am blue."

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# HTML Template
PAGINATED_DIRECT_TEMPLATES = ("categories", "archives")
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives")
