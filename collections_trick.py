#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 计数器（Counter）
# Counter作为字典dict()的一个子类用来进行hashtable计数，将元素进行数量统计，计数后返回一个字典，键为元素，值为元素个数
from collections import Counter

str1 = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
d = {"1":3, "3":2, "17":2}

#Counter获取各元素的个数，返回字典
print("Counter(s):", Counter(str1)) # Counter(s): Counter({'b': 4, 'c': 4, 'a': 3, 'd': 1})
print("Counter(li):", Counter(li)) # Counter(li): Counter({'b': 3, 'a': 2, 'c': 1})
print("Counter(d):", Counter(d)) # Counter(d): Counter({'1': 3, '3': 2, '17': 2})

# most_common(int)按照元素出现的次数进行从高到低的排序，返回前int个元素的字典
d1 = Counter(str1)
print(d1.most_common(2)) # [('b', 4), ('c', 4)]

# elements返回经过计算器Counter后的元素，返回的是一个迭代器
print(list(d1.elements())) # ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
print("|".join(d1.elements())) # a|a|a|b|b|b|b|c|c|c|c|d

# update和set集合的update一样，对集合进行并集更新
d1.update("sas")
print(d1) # Counter({'a': 4, 'b': 4, 'c': 4, 's': 2, 'd': 1})


# 双向队列（deque）
# 定义长度，可用于历史记录的查询
# deque除了实现list的append()和pop()外，还支持appendleft()和
# popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque

q = deque([7,8,9],maxlen=10)
q.append(1)
print(q)


# 默认字典（defaultdict）
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A') # defaultdict的参数是一个产生默认值的工厂函数
dd['key1'] = 'abc'
print(dd['key1']) # key1存在   返回'abc' 
print(dd['key2']) # key2不存在，返回默认值 'N/A'

s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(d) # defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
print(d) # defaultdict(<class 'set'>, {'red': {1, 3}, 'blue': {2, 4}})

# 有序字典（OrderedDict）
# 默认使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
# 但python3.6之后dict的key是有序的，顺序为添加Key的顺序
from collections import OrderedDict

dic2 = OrderedDict()  
dic2['a'] = '123'  
dic2['b'] = 'jjj'  
dic2['d'] = 'abc'  
dic2['c'] = '999'  
for k, v in dic2.items():  # 顺序为添加key的顺序
    print('有序字典：%s:%s' %(k,v))

# 可命名元组（namedtuple）
from collections import namedtuple
# 返回一个tuple类型，可以通过自定义的属性访问而不是索引
User = namedtuple('User', ['age','name'])
user = User(19,'xiaoming') # <class 'type'> User(age=19, name='xiaoming')
print(type(User), user)
print(user.name)
print(user.age)


"""
有多个字典或者映射，想把它们合并成为一个单独的映射，有人说可以用update进行合并，
这样做的问题就是新建了一个数据结构以致于当我们对原来的字典进行更改的时候不会同步。
如果想建立一个同步的查询方法，可以使用ChainMap

增删改的操作都只会针对该对象的第一个字典，其余字典不会发生改变，
但是如果是查找，则会在多个字典中查找，直到找到第一个出现的key为止
"""
from collections import ChainMap
a = {"x":1, "z":3}
b = {"y":2, "z":4}
c = ChainMap(a, b)
print(c) # ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})
print(c.maps) # [{'x': 1, 'z': 3}, {'y': 2, 'z': 4}]
print("x: {}, y: {}, z: {}".format(c["x"], c["y"], c["z"])) # x: 1, y: 2, z: 3

# 在字典列表头部插入字典，如果其参数为空，则会默认插入一个空字典，并且返回一个改变后的ChainMap对象
print(c.new_child({'a':1})) # ChainMap({'a': 1}, {'x': 1, 'z': 3}, {'y': 2, 'z': 4})