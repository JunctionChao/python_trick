# 多个装饰器在装饰时是从下往上装饰，在执行时是从上往下执行
def set_func1(func):
    print("---开始装饰1---")
    def call_func(*args, **kwargs):
        print("执行装饰器1的功能")
        ret = func(*args, **kwargs) # 这里是拆包
        return ret
    return call_func

def set_func2(func):
    print("---开始装饰2---")
    def call_func(*args, **kwargs):
        print("执行装饰器2的功能")
        ret = func(*args, **kwargs) # 这里是拆包
        return ret
    return call_func

@set_func1 # test = setset_func1(test1)
@set_func2 # test1 = set_func2(test)
def test(*args, **kwargs):
    print(args, kwargs)
    for i in range(100000):
        pass
    return "test_finished"


if __name__ == '__main__':
    r = test(1, 2, 3, a=1, b=2)
    print(r)

"""
---开始装饰2---
---开始装饰1---
执行装饰器1的功能
执行装饰器2的功能
(1, 2, 3) {'a': 1, 'b': 2}
test_finished
"""