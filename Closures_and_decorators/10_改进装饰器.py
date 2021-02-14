# 我们之前实现的装饰器有个缺点，会遮盖了被装饰函数的 __name__ 和 __doc__ 属性
# 通过functools.wraps 装饰器把相关的属性还原会来

import time
from functools import wraps

def set_func(func):
    @wraps(func)
    def call_func(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs) # 这里是拆包
        stop_time = time.time()
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
    print(test.__name__) # test
    r = test(1, 2, 3, a=1, b=2)
    print(r)