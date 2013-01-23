# -*- coding: utf-8 -*- #
from __future__ import unicode_literals, print_function

AUTHOR = 'Mike Kazantsev'
SITENAME = 'My blog_title_here'

SITEURL = 'http://cane:8000'

THEME = 'themes/mockingbird'
TIMEZONE = 'Asia/Yekaterinburg'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_ATOM = FEED_ATOM
FEED_ALL_RSS = FEED_RSS

DISPLAY_PAGES_ON_MENU = False

LINKS = [
	('Homepage', 'fraggod.net') ]


PLUGINS = ['pelican.plugins.sitemap']

SITEMAP = dict(
	format='xml',
	priorities=dict(
		articles=0.9,
		pages=0.3,
		indexes=0.8 ),
	changefreqs=dict(
		articles='monthly',
		pages='monthly',
		indexes='weekly' ) )
