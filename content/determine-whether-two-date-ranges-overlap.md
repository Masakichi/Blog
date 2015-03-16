Title: 判断两个时间段是否有交集
Date: 2015-01-06 22:37
Category: Other
Tags: algorithm
Slug: determine-whether-two-date-ranges-overlap

已知两个时间片段A、B的起止时间分别是 A.begin_time，A.end_time、B.begin_time，B.end_time 求 AB 是否有交集。tl;dr: `(A.end_time >= B.begin_time) and (B.end_time >= A.begin_time)`

Step 1. 直接求交集的话遇到的判断情况比较多，故先求没有交集的情况。只要 `A.end_time < B.begin_time or B.end_time < A.begin_time` 即可。

Step 2. 有交集的情况就是 Step 1的情况取反即：`not (A.end_time < B.begin_time or B.end_time < A.begin_time)`

Step 3. 到 Step 2 为止就可以判断是否有交集了，不过根据德摩根律[`Not (A or B) <=> Not A and Not B `]可以化简得到：`(A.end_time >= B.begin_time) and (B.end_time >= A.begin_time)`

Python 代码如下：

```python
#!/usr/bin/python

from datetime import datetime
from collections import namedtuple

Range = namedtuple('Range', ['begin_time', 'end_time'])

def has_overlap(A, B):
    if (A.end_time >= B.begin_time) and (B.end_time >= A.begin_time):
        return True
    else:
        return False
        
# Test1 A1: 2015-1-6 ~ 2015-1-9, B1: 2015-1-10 ~ 2015-1-15
A1 = Range(begin_time=datetime(2015, 1, 6), end_time=datetime(2015, 1, 9))
B1 = Range(begin_time=datetime(2015, 1, 10), end_time=datetime(2015, 1, 15))
print has_overlap(A1, B1) #False

# Test2 A2: 2015-1-6 ~ 2015-1-9, B2: 2015-1-8 ~ 2015-1-15
A2 = Range(begin_time=datetime(2015, 1, 6), end_time=datetime(2015, 1, 9))
B2 = Range(begin_time=datetime(2015, 1, 8), end_time=datetime(2015, 1, 15))
print has_overlap(A2, B2) #True

# Test3 A3: 2015-1-6 ~ 2015-1-9, B3: 2015-1-7 ~ 2015-1-8
A3 = Range(begin_time=datetime(2015, 1, 6), end_time=datetime(2015, 1, 9))
B3 = Range(begin_time=datetime(2015, 1, 7), end_time=datetime(2015, 1, 8))
print has_overlap(A3, B3) #True
```

参考：

- [Determine Whether Two Date Ranges Overlap](http://stackoverflow.com/questions/325933/determine-whether-two-date-ranges-overlap)
- [Efficient date range overlap calculation in python?](http://stackoverflow.com/questions/9044084/efficient-date-range-overlap-calculation-in-python)