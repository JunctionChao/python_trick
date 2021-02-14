"""
这里返回都是函数，在后续会被调用使用，并且用到和它同级的其他数据，因此和它同级别作用域的其他数据也会被系统保留
"""

def line(k, b):
    def res(x):
        return k * x + b
    return res


def make_averager():
    series = [] # 称之为自由变量
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


if __name__ == '__main__':
    line1 = line(5, 2)
    print(line1(6)) # 32
    print(line1(7)) # 37

    print(line1.__code__.co_varnames) # ('x',)  局部变量
    print(line1.__code__.co_freevars) # ('b', 'k')  自由变量

    avg = make_averager()
    print(avg(1)) # 1.0
    print(avg(2)) # 1.5
    print(avg(3)) # 2.0

    print(avg.__code__.co_varnames) # ('new_value', 'total')  局部变量
    print(avg.__code__.co_freevars) # ('series',)  自由变量
