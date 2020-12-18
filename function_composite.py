#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-12-30
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://mathieularose.com/function-composition-in-python/

def compose2(f, g):
    return lambda x: f(g(x))  # 返回的是一个函数

def double(x):
    return x * 2

def inc(x):
    return x + 1


inc_and_double = compose2(double, inc)
print(inc_and_double(10)) # double(inc(10))


def dec(x):
    return x - 1

inc_double_and_dec = compose2(compose2(dec, double), inc)
print(inc_double_and_dec(10)) # dec(double(inc(10)))


import functools

# def compose(*functions):
#     def compose2(f, g):
#         return lambda x: f(g(x))
#     return functools.reduce(compose2, functions, lambda x: x)

# 同上
def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x) # 这个最后的匿名函数可以不需要的

inc_double_and_dec = compose(dec, double, inc)
print(inc_double_and_dec(10))

# 多参数函数
def mulit_para_compose(*functions):
    if funcs:
        return reduce(lambda f, g: lambda *a, **kw: f(g(*a, **kw)), funcs)
    else:
        raise ValueError('Composition of empty sequence not supported.')