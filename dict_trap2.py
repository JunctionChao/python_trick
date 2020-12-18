#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-19
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# python内置函数在dict上的应用

# 1. map
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.9, 2))

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
new_prices = dict(map(discount, prices.items()))
print(new_prices) # {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}

# 2. filter
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
low_price = dict(filter(lambda kv: kv[1] < 0.4, prices.items()))
print(low_price) # {'orange': 0.35, 'banana': 0.25}

# 3. collections.ChainMap 可以将多个字典连接起来
from collections import ChainMap
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
chained_dict = ChainMap(fruit_prices, vegetable_prices)
print(chained_dict) # ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})
for k, v in chained_dict.items():
    print(k, v)
"""
onion 0.55
apple 0.4
orange 0.35
pepper 0.2
"""

# 4. itertools
# 4.1 Cyclic Iteration With cycle() 循环迭代
from itertools import cycle
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
times = 3  # Define how many times you need to iterate through prices
total_items = times * len(prices)
for item in cycle(prices.items()):
    if not total_items:
        break
    total_items -= 1
    print(item)

"""
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
"""

# 4.2 Chained Iteration With chain() 链接多个迭代器
from itertools import chain
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55, 'tomato': 0.42}
for item in chain(fruit_prices.items(), vegetable_prices.items()):
    print(item)
"""
('apple', 0.4)
('orange', 0.35)
('banana', 0.25)
('pepper', 0.2)
('onion', 0.55)
('tomato', 0.42)
"""

# 5. Using the Dictionary Unpacking Operator (**) 字典解包操作
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
# How to use the unpacking operator **
print({**vegetable_prices, **fruit_prices}) # {'pepper': 0.2, 'onion': 0.55, 'apple': 0.4, 'orange': 0.35}
# You can use this feature to iterate through multiple dictionaries
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)
"""
pepper -> 0.2
onion -> 0.55
apple -> 0.4
orange -> 0.35
"""