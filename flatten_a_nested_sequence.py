#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-10-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://github.com/dabeaz/python-cookbook/blob/master/src/4/how_to_flatten_a_nested_sequence/example.py

# Example of flattening a nested sequence using subgenerators

"""
yield from x 表达式对 x 对象所做的第一件事是，调用 iter(x)，从中获取迭代器。
因此，x 可以是任何可迭代的对象

在生成器 gen 中使用 yield from subgen()
时，subgen 会获得控制权，把产出的值传给 gen 的调用方，即调用方
可以直接控制 subgen。与此同时，gen 会阻塞，等待 subgen 终止
"""
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)