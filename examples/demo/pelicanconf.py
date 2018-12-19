#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import sys
import os

sys.path.append(os.curdir)


AUTHOR = "Ashwin Vishnu"
SITENAME = "Pelican | Bluedrop theme"
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
STATIC_PATHS = ["./images"]

# Backdrop specific variables
SITESUBTITLE = ""
SITE_DESCRIPTION = "This is a simple demo of the capabilities of the bluedrop theme"

PROFILE_IMAGE = "/images/python-powered-h-50x65.png"
EMBLEMS = (("/images/python-powered-h.svg", "https://python.org"),)
FAVICON = "/images/python-powered-h-50x65.png"

# Carousel
CAROUSEL = (
    ("Python Powered", "/images/python-logo-master-v3-TM-flattened.png",
     "https://python.org"),
    ("How Pelican works", "/images/pelican-works.png",
     "https://docs.getpelican.com"),
)

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com"),
    ("Python.org", "https://python.org/"),
)

# Social widget
EMAIL = "me@example.com"
GPG = "https://sks-keyservers.net/pks/lookup?op=vindex&search=0x2BF1534545A73FAD"
MASTODON = "https://scholar.social/@ashwinvis"
SOCIAL = (
    ("Github", "https://github.com/ashwinvis"),
    ("Gitlab", "https://source.coderefinery.org/ashwinvis/"),
    ("Bitbucket", "https://bitbucket.org/avmo"),
    ("LinkedIn", "https://www.linkedin.com/in/ashwinvishnu/"),
)
RESEARCH = (
    ("Zotero", "https://zotero.org/ashwinvis"),
    ("ResearchGate", "https://www.researchgate.net/profile/Ashwin_Vishnu_Mohanan"),
    ("Google-Scholar", "https://scholar.google.se/citations?user=zv4wwKoAAAAJ"),
    ("ORCID", "https://orcid.org/0000-0002-2979-6327"),
    ("Zenodo", "https://zenodo.org/search?page=1&size=20&q=Mohanan,%20Ashwin%20Vishnu"),
)

YEAR = date.today().year
LICENSE = r"""
    <a
    href="https://github.com/ashwinvis/pelican-bluedrop/blob/develop/LICENSE">
    CC-BY-SA 4.0</a>
    """

# Plugins
PLUGIN_PATHS = ["../../plugins"]
PLUGINS = ["sitemap", "representative_image", "tipue_search"]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.7, "indexes": 0.5, "pages": 0.3},
    "changefreqs": {"articles": "monthly", "indexes": "monthly", "pages": "monthly"},
}

# Pagination
DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

# HTML Template
PAGINATED_DIRECT_TEMPLATES = ("categories", "archives", "index", "pages")
DIRECT_TEMPLATES = ("index", "tags", "categories", "archives", "search")
