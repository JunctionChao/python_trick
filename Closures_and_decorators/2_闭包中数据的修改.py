"""
在闭包中修改自由变量时，对数字、字符串、元组等不可变类型必须使用nonlocal声明
而对于可变类型则不需要，因为可变类型的地址始终保持不变
"""

def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1 # count = count + 1，其实会隐式创建局部变量 count
        total += new_value
        return total / count
    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(1)) # 1.0
    print(avg(2)) # 1.5
    print(avg(3)) # 2.0