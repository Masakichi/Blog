Title: The Hacker’s Guide to Python学习笔记：第二章
Date: 2014-05-11 14:56
Category: Python
Tags: notes
Slug: notes-of-the-hackers-guide-to-python-chapter-2

**第二章：模块和库**

##导入（import）系统

`pass #太复杂，以后看好了`

##标准库

不要重复造轮子。标准库有的话，一定记得用标准库。

下面是一些**必须**知道的标准库：（当我了解的差不多时，我会加上内容，暂时只列出名称。）

* atexit
* argparse
* bisect
* calendar
* codecs
* collections
* copy
* csv
* datetime
* fnmatch
* glob
* io
* json
* logging
* multiprocessing
* operator
* os
* random
* re
* select
* shutil
* signal
* tempfile
* threading
* urllib
* uuid

##外部库

外部库的选择有一定风险，如更新不勤、兼容性、文档不全、迁移风险等等，以下列出一些选择的标准：

* 最好兼容Python 3
* 开发活跃，GitHub等开源站点去评估。
* 维护活跃，开发者对bug的反应程度。
* 是否被一些流行的发行版打包发行。这样即便遇到问题你也不是一个人在战斗。
* API兼容性的保证，API的经常变动无疑是个噩梦。

**Tips:**

最好对外部库做一次封装，设计一套自己的API，不要让外部库触及自己的核心代码（即自己的代码不关心使用了何种外部库），否者更换外部库的话工作量会很大。

##框架

常用的Web框架：

* Django
* Flask
* Pylons
* TruboGears
* Tornado
* Zope
* Plone

时间驱动框架：

* Twisted
* Circuits

**Tips:**

> 框架是把双刃剑，一方面可以迅速建立原型，快速开发，不过想要转换框架的话，基本上得重写代码。

> 一个框架提供的东西越少，那么你以后需要解决的问题也越少。

##设计、管理API

`pass #等老子有自信能写API的时候来补。`

##其他资料

* The Python Standard Library By Example：[ClickMe](http://doughellmann.com/pages/python-standard-library-by-example.html)
* Python Module of the Week：[ClickMe](http://pymotw.com/2/)