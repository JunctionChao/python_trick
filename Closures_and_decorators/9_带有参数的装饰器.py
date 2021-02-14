def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("---权限级别1,验证---")
            elif level_num == 2:
                print("---权限级别2,验证---")
            else:
                print("---其他权限级别,验证---")
            ret = func(*args, **kwargs)
            print("函数执行完后的装饰功能")
            return ret

        return call_func
    return set_func

@set_level(1)  # 用set_level(1)的返回函数对test1进行装饰
def test1(*args, **kwargs):
    print(args, kwargs)
    return "test1 finished"

@set_level(2)
def test2(*args, **kwargs):
    print(args, kwargs)
    return "test2 finished"


if __name__ == '__main__':
    t1 = test1(1, 2, a=1, b=2)
    print(t1)
    """
    ---权限级别1,验证---
    (1, 2) {'a': 1, 'b': 2}
    函数执行完后的装饰功能
    test1 finished
    """

    t2 = test2(3, 4, a=3, b=4)
    print(t2)
    """
    ---权限级别2,验证---
    (3, 4) {'a': 3, 'b': 4}
    函数执行完后的装饰功能
    test2 finished
    """