#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gimo'
SITENAME = u"Gimo's Blog"
SITEURL = 'http://gimo.me'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
# SOCIAL = (('V2EX', 'http://v2ex.com/member/jyjmrlk'),
#          ('Douban', 'http://douban.com/people/62970444'),
#          ('Github', 'http://github.com/masakichi'))

DEFAULT_PAGINATION = 5
# PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)

DISQUS_SITENAME = "gimosblog"
#DUOSHUO_SITENAME = "gimo"

#PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

THEME = "/Users/Gimo/Dropbox/Github/pelipress"
PLUGIN_PATHS = ['/Users/Gimo/Dropbox/Github/pelican-plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml'}
SITESEARCH = '//google.com/search'
#GOOGLE_ANALYTICS = 'UA-50840195-1'

GITHUB_USER = "masakichi"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False
MENUBRAND = [("Gimo's Blog", '/')]
SOCIAL_SIDEBAR_TOP = (
    ('Weibo', 'http://weibo.com/jiangyuanji', '<i class="icon-weibo"></i>'),
    ('Twitter', 'http://twitter.com/gimo_me', '<i class="icon-twitter"></i>'),
    ('Github', 'http://github.com/masakichi', '<i class="icon-github"></i>'),
    ('RSS', '/feeds/all.rss.xml', '<i class="icon-rss"></i>'))
# code block with line numbers
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# date format
DATE_FORMATS = {
        'cn': '%Y-%m-%d'}

# favicon
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'}
        }
