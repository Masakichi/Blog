Title: 计划写一个HTTP页面的Parser
Date: 2014-07-22 17:27
Category: Python
Tags: readability
Slug: plan-to-write-a-html-parser
Status: draft

前段时间在写一个自用的Read it later类型的Web App，遗憾的是核心部分的页面抓取代码只是调用了Readability的Parser API。所以想花点时间自己写一个parser。幸运的是Readability曾经开源过代码，很多人也port过。所以可以做一些参考。下面列举一些收集的资源。

## 原理
* [Instapaper的网页内容文本自动抓取技术是什么原理，我看着好神奇。我试了好多网页，对于网页中对文本内容识别的都是惊人的准确。我问身边专门做数据采集的同事都不知道如何实现。](http://www.v2ex.com/t/10934)
* [花了3个晚上，把readability最新的1.7.1转成了python版的](http://www.v2ex.com/t/29123)
* [Pocket, Instapaper, readability是如何快速准确抓取某个页面正文内容的?](http://www.v2ex.com/t/67099)
* [网页正文抽取工具](http://www.zhizhihu.com/html/y2013/4202.html)
* [What algorithm does Readability use for extracting text from URLs?](http://stackoverflow.com/questions/3652657/what-algorithm-does-readability-use-for-extracting-text-from-urls)

## 开源方案
* [gfxmonk/python-readability](https://github.com/gfxmonk/python-readability)
* [Decruft](http://www.minvolai.com/blog/decruft-arc90s-readability-in-python/)
* [buriy/python-readability](https://github.com/buriy/python-readability)
* [wallabag/wallabag](https://github.com/wallabag/wallabag)
* [kingwkb/readability](https://github.com/kingwkb/readability)

## Demo
* [http://yanghao.org/tools/readability](http://yanghao.org/tools/readability)

## 目标
在以上开源代码实现的功能上实现如下功能：

* 提供特定网页的recipe，更优化解析。
* 转化为markdown的功能。
* 分词功能，提取关键字
* 缓存功能
* 提取时间、阅读方向、图片、作者、摘要等信息
* 对于分页文章的提取

## 可能出现问题
* 性能问题
* 编码问题
* 错误处理问题
* 代理问题
* 登陆问题［可选］
* 时效性［可选］
