#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ref: https://realpython.com/iterate-through-dictionary-python/
"""
字典使用陷阱

1.首先遍历字典时不能同时添加新的键
    无论何时往字典里添加新的键，Python 解释器都可能做出为字典扩容的决定，
扩容导致的结果就是要新建一个更大的散列表，并把字典里已有的元素添加到新表里。
这个过程中可能会发生新的散列冲突，导致新散列表中键的次序变化，那么这个循环
很有可能会跳过一些键——甚至是跳过那些字典中已经有的键

2.遍历过程中也不能删除键

d = {'k1': 'v1', 'k2': 'k2', 'k3': 'v3'}

for k in d.keys():
    if k == "k2":
          del d[k]

for k,v in d.items():
    if k == "k2":
        del d[k]

上述方法都会报错
Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    for k in d.keys():
RuntimeError: dictionary changed size during iteration
"""

# 正确做法
# 2.1 list(d.keys())返回整个keys迭代器的列表
d = {'k1': 'v1', 'k2': 'k2', 'k3': 'v3'}
for k in list(d.keys()): # 这个遍历跟字典d没关系了,遍历的是keys组成的列表
    if k == "k2":
        del d[k]
print(d) # {'k1': 'v1', 'k3': 'v3'}

# 2.2 解析式方式
d = {'k1': 'v1', 'k2': 'k2', 'k3': 'v3'}
d = {k: v for k, v in d.items() if k != "k2"}
print(d) # {'k1': 'v1', 'k3': 'v3'}

# 2.3 利用字典键值视图支持set运算操作 
# key-view objects support set operations like unions, intersections, and differences
d = {'k1': 'v1', 'k2': 'k2', 'k3': 'v3'}
d = {k: d[k] for k in d.keys() - {'k2'}}
print(d)


# 3遍历修改键值的几种方法

# 3.1原始方式修改
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
print(prices) # {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}


# 3.2字典解析式方式
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
prices = {k: round(v * 0.9, 2) for k, v in prices.items()}
print(prices) # {'apple': 0.36, 'orange': 0.32, 'banana': 0.23}


# 4.字典排序
# 字典本身是无序的，但在python3.6以后，python实现字典背后的数据结构是有序的(字典每次打印的次序是一样的)
# https://www.cnblogs.com/xieqiankun/p/python_dict.html
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
# sorted(incomes)返回的是个列表: ['apple', 'banana', 'orange']
sorted_income = {k: incomes[k] for k in sorted(incomes)} #也是按key排序
print(sorted_income) # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}

# 4.1 按key排序
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: incomes[k] for k in sorted(incomes.keys())}
print(sorted_income) # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}
sorted_income = dict(sorted(incomes.items()))
print(sorted_income) # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}

# 4.2 按value排序
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
sorted_income = {k: v for k, v in sorted(incomes.items(), key=lambda kv: kv[1])}
print(sorted_income) # {'orange': 3500.0, 'banana': 5000.0, 'apple': 5600.0}
sorted_income = {k: incomes[k] for k in sorted(incomes, key=lambda k: incomes[k])}
print(sorted_income) # {'orange': 3500.0, 'banana': 5000.0, 'apple': 5600.0}
sorted_income = {k: incomes[k] for k in sorted(incomes, key=lambda k: incomes[k], reverse=True)} # 逆序
print(sorted_income) # {'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}


# 5.破坏性迭代字典(遍历并逐一清空)
# Iterating Destructively With .popitem()
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break