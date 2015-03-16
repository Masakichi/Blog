Title: The Hacker’s Guide to Python学习笔记：第一章
Date: 2014-05-10 15:48
Category: Python
Tags: notes
Slug: notes-of-the-hackers-guide-to-python-chapter-1

**第一章：开始项目**

##Python版本

实在有必要的话，支持2.6版本，否则从2.7开始支持。为了以后的发展，支持3.3及以后版本。

##组织代码

如图所示：

![project-layout]({filename}/images/project-layout.png)

至于其他文件，如图像、脚本、配置文件等。可以按照如下目录放置。

* etc 放置配置文件。
* tools 放置shell脚本或者相关工具。
* bin 二进制文件
* data 放置图像等数据文件。

文件已特点命名，而不是类型：functions.py、exceptions.py毫无意义。

##关于版本号

详情看[PEP 440](http://legacy.python.org/dev/peps/pep-0440/)。

##代码风格

详情看[PEP 8](http://legacy.python.org/dev/peps/pep-0008/)。主旨如下：

* 4空格缩进。
* 每行最多79字符。
* 顶层类、函数定义前空两行。
* 采用ASCII或UTF-8文件编码。
* 在文件开头（当然在文件注释、文档之后）import模块，且每行只导入一个模块。导入顺序：标准库、第三方库、本地库。
* 括号（(),[],{}）之间不留多余空格，逗号之前不留空格。
* 类的命名使用驼峰式（CamelCase），exceptions指出Error（如果可以的话），函数命名使用小写下划线的格式（separated_by_underscores），私有函数、属性使用下划线开头（_private）。