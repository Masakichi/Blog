Title: Python标准库笔记-os.path
Date: 2014-05-20 18:44
Category: Python
Tags: notes, module
Slug: notes-of-the-python-standard-library-os-path

**作用：**处理、构建、测试文件名及路径

**1.4及以后版本可用**

##处理路径

###split(path)

作用：用于分割路径。

input:

```python
import os.path
```

output:

```python
"/one/two/three" : "(’/one/two’, ’three’)"



###splittext(path)
作用：类似于split()，不过以扩展名（如.txt）作为分割依据。

###commonprefix(path)

##构造路径

###join(path1[, path2[, ...]])

作用：合成路径。

input:

```python
import os.path

output:

```python

###expanduser(path)

作用：将'~'转化为家目录的路径。

###expandvars(path)

作用：通过环境变量生成路径？

input:

```python
import os.path
```

output:

```python
/path/to/VALUE
```
##规范化路径

###normpath(path)

作用：规范化路径。

input:

```python
import os.path
```

output:

```python
one//two//three : one/two/three
```
###abspath(path)

作用：将相对路径转化为绝对路径。

input:

```python
import os.path
```

output:

```python
"." : "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/ospath"
```
##文件时间

###getatime(path):读取时间
###getmtime(path):修改时间
###getctime(path):元数据修改时间（UNIX－like）或文件生成时间（Windows）？

##测试文件

###isabs(path)
###isfile(path)
###isdir(path)
###islink(path)
###ismount(path)
###exists(path)
###lexists(path):link exists?

##walk()??