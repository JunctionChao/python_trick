#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref: https://www.datacamp.com/community/tutorials/18-most-common-python-list-questions-learn-python

# How To Split A Python List Into Evenly Sized Chunks
# 将列表分成均匀大小的块

# 这里要注意[iter(x)]*3是浅拷贝，所有iter(x)都指向同一地址
# 不足块长度的舍弃，这是zip的特性
x = [1,2,3,4,5,6,7,8,9,10,11]
# Split `x` up in chunks of 3
y = zip(*[iter(x)]*3)

# Use `list()` to print the result of `zip()`
print(list(y)) # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


# Method to split up your lists into chunks
def chunks(l, chunkSize):
    """Yield successive chunkSize-sized chunks from list."""
    for i in range(0, len(l), chunkSize):
        yield l[i:i + chunkSize]

# Use your `chunks` function to print out chunks of the same size
import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))

"""
[range(10, 20),
 range(20, 30),
 range(30, 40),
 range(40, 50),
 range(50, 60),
 range(60, 70),
 range(70, 75)]
"""
l = range(10, 75)
chunks_size = 10
res = [l[i:i+chunks_size] for i in range(0, len(l), chunks_size)]
pprint.pprint(res) # 结果同上


# How To Create Flat Lists Out Of Lists 展平列表
listOfLists = [[1,2],[3,4],[5,6]]

# Flatten out your original list of lists with `sum()`
print(sum(listOfLists, [])) # [1, 2, 3, 4, 5, 6]

# You can reduce the lists of lists of lists like this
from functools import reduce
print(reduce(lambda x, y: x+y, listOfLists)) # [1, 2, 3, 4, 5, 6]

# Or you can use list comprehension
print([item for sublist in listOfLists for item in sublist]) # [1, 2, 3, 4, 5, 6]


# How To Get An Intersection Of Two Python Lists
list2 = [[13, 32], [7, 13, 28], [1, 6]]
list1 = [7, 28, 1, 6, 9]
intersect_list2 = [list(filter(lambda x: x in list1, sublist)) for sublist in list2]
print(intersect_list2) # [[], [7, 28], [1, 6]]

"""
Intersection of two lists including duplicates, like this

>>> a = [1,1,1,2,3,4,4]
>>> b = [1,1,2,3,3,3,4]
[1,1,2,3,4]
"""
from collections import Counter
a = [1,1,1,2,3,4,4]
b = [1,1,2,3,3,3,4]
c = list((Counter(a) & Counter(b)).elements())
print(c) # [1, 1, 2, 3, 4]


b_, c = b.copy(), list()
for x in a:
    if x in b_:
        b_.remove(x)
        c.append(x)
print(c) # [1, 1, 2, 3, 4]


# 计算迭代器的长度
sum((i for _ in range(8))) # 8

# 读取文件行数
with open("filename", "r+") as f:
    print(sum(1 for line in f))
