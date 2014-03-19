# -*- coding: utf-8 -*- #
from __future__ import unicode_literals, print_function

AUTHOR = 'Mike Kazantsev'
SITENAME = 'My blog_title_here'

SITEURL = 'http://cane:8000'

THEME = 'themes/mockingbird'
TIMEZONE = 'Asia/Yekaterinburg'

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'Uncategorized'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

FEED_MAX_ITEMS = 10
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag/%s.rss.xml'

DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['images', 'misc']
# EXTRA_PATH_METADATA = {
# 	'extra/robots.txt': {'path': 'robots.txt'} }
# TEMPLATE_PAGES = {
# 	'src/books.html': 'dest/books.html',
# 	'src/resume.html': 'dest/resume.html',
# 	'src/contact.html': 'dest/contact.html' }

LINKS = [
	('Homepage', 'fraggod.net') ]


PLUGINS = [
	'plugins.html_rst_directive',
	'plugins.sitemap' ]

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
