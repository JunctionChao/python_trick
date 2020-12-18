#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-09
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 1. 重复元素判定
# 以下方法可以检查给定列表是不是存在重复元素，它会使用 set() 函数来移除所有重复元素
def all_unique(lst):
    return len(lst) == len(set(lst))

x = [1,1,2,2,3,2,3,4,5,6]
y = [1,2,3,4,5]
all_unique(x) # False
all_unique(y) # True


# 2. 字符元素组成判定
# 检查两个字符串的组成元素是不是一样的
from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)

anagram("abcd3", "3acdb") # True


# 3. 内存占用
# 下面的代码块可以检查变量 variable 所占用的内存。
import sys 

variable = 30 
print(sys.getsizeof(variable)) # 28


# 4. 字节占用
# 下面的代码块可以检查字符串占用的字节数。
def byte_size(string):
    return(len(string.encode('utf-8')))

byte_size('😀') # 4
byte_size('Hello World') # 11   


# 5. 打印 N 次字符串
# 该代码块不需要循环语句就能打印 N 次字符串。
n = 2; 
s ="Programming"; 

print(s * n); # ProgrammingProgramming  


# 6. 大写第一个字母
# 以下代码块会使用 title() 方法，从而大写字符串中每一个单词的首字母。
s = "programming is awesome"
print(s.title())# Programming Is Awesome


# 7.分块
# 以下方法使用 range() 将列表分块为指定大小的较小列表
from math import ceil # 返回数字的上入整数
def chunk1(lst, size):
    return list(
        map(lambda x: lst[x*size:x*size+size], range(0, ceil(len(lst) / size)))
        )

# 直接使用列表生成式 （map可以转换为列表生成式）
def chunk2(lst, size):
    return [lst[i*size:i*size+size] for i in range(0, ceil(len(lst) / size))]

print(chunk1([1,2,3,4,5], 2))
print(chunk2([1,2,3,4,5], 2))


# 8.压缩或者过滤
# 以下方法使用 fliter() 删除列表中的错误值（如：False, None, 0 和“”）
def compact(lst):    
    return list(filter(bool, lst))    
print(compact([0, 1, False, 2, ' ', 3, 'a',  's', 34]))


# 10.链式比较
# 以下代码可以在一行中用各种操作符进行多次比较。
a = 3    
print(2 < a < 8) # True    
print(1 == a < 2) # False


# 14. 展开列表
# 该方法将通过递归的方式将列表的嵌套展开为单个列表。
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(lst):
    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst))))
    return result

print(deep_flatten([1, [2], [[3, [6, 7]], 4], 5]))


# 15. 列表的差
# 该方法将返回第一个列表的元素，其不在第二个列表内。如果同时要反馈第二个列表独有的元素，还需要加一句 set_b.difference(set_a)。

def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)

print(difference([1,2,3], [1,2,4]) )# [3]


# 17. 链式函数调用
# 你可以在一行代码内调用多个函数。

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9 