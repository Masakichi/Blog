Title: 使用Pelican生成静态博客并托管到Github Pages
Date: 2014-05-06 19:24
Category: Python
Tags: Pelican
Slug: Use-Pelican-generate-static-blog-and-deploy-on-Github-Pages

##介绍
Pelican是用Python开发的一款静态博客生成工具。支持reStructuredText，Markdown，AsciiDoc格式。非常方便设置、生成、部署。

source code: [Pelican](http://github.com/getpelican/pelican)

官方文档：[Pelican](http://docs.getpelican.com/en/3.3.0/)

##安装
使用pip：`pip install pelican`

如果实用Markdown格式：`pip install Markdown`

##快速使用
`pelican-quickstart` 以上命令将生成一个站点目录
```
yourproject/
├── content
│   └── (pages)
├── output
├── develop_server.sh
├── fabfile.py
├── Makefile
├── pelicanconf.py       # Main settings file
└── publishconf.py       # Settings to use when ready to publish
```
生成html：`make html`

自动生成：`make regenerate`

建立本地服务器：`make serve`

##写文章(以Markdown为例)
###文章：在content中创建article.md，内容如下
```
Title: My super title
Date: 2010-12-03 10:20
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Author: Alexis Metaireau
Summary: Short version for index and feeds

This is the content of my super blog post.
```
###页面：在content中创建pages目录，创建about.md，当然格式和文章一样。

##主题
[官方主题库](https://github.com/getpelican/pelican-thems)

详情见如上链接。本博客使用的主题叫pelipress。

##附设置文件以供参考
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gimo'
SITENAME = u"Gimo's Blog"
SITEURL = 'http://gimo.me'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('V2EX', 'http://v2ex.com/member/jyjmrlk'),
          ('Douban', 'http://douban.com/people/62970444'),
          ('Github', 'http://github.com/masakichi'))

DEFAULT_PAGINATION = 10

THEME = "/Users/Gimo/pelican-themes/pelipress"

GITHUB_USER = "masakichi"
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = False
GITHUB_SHOW_USER_LINK = False
MENUBRAND = [('Blog', '/'), ]
SOCIAL_SIDEBAR_TOP = (
    ('Weibo', 'http://weibo.com/jiangyuanji', '<i class="icon-weibo"></i>'),
    ('Twitter', 'http://twitter.com/gimo_me', '<i class="icon-twitter"></i>'),
    ('Github', 'http://github.com/masakichi', '<i class="icon-github"></i>'),
    ('RSS', '/feeds/all.rss.xml', '<i class="icon-rss"></i>'))
# code block with line numbers
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

```

##托管到Github Pages
###创建Repo
[点击这里](http://github.com/new)，名字必须是xxx.github.io，其中xxx为你的ID。

###Push博客目录即是output目录
```
cd output
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/xxx/xxx.github.io.git
git push -u origin master
```
几分钟后，访问[http://masakkichi.github.io](http://masakichi.github.io)，就可以访问了，不要着急，有点延时是正常的。

###绑定域名
在output目录下创建CNAME文件，在里面写入要绑定的域名，如下：

`gimo.me`

*注意：*

如果是顶级域名，A记录到：`192.30.252.153`
二级域名等，CNAME记录到：`xxx.github.io`，xxx为ID
