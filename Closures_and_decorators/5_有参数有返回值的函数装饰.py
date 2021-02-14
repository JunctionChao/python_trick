# 对有参数有返回值的函数进行装饰
# 通用装饰器

import time

def set_func(func):
    def call_func(*args, **kwargs):
        print('执行前：', func.__name__)
        start_time = time.time()
        ret = func(*args, **kwargs) # 这里是拆包
        stop_time = time.time()
        print('执行后：', func.__name__)
        print('函数 {} ran in: {} sec'.format(func.__name__, stop_time-start_time))
        return ret
    return call_func

@set_func  # 等价于 test = set_func(test)
def test(*args, **kwargs):
    print(args, kwargs)
    for i in range(100000):
        pass
    return "test_finished"


if __name__ == '__main__':
    print(test.__name__) # call_func  这里修改了test的__name__属性
    r = test(1, 2, 3, a=1, b=2)
    print(r)