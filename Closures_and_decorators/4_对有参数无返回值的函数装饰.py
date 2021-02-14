import time

def set_func(func):
    def call_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs) # 这里是拆包
        stop_time = time.time()
        print('函数 {} ran in: {} sec'.format(func.__name__, stop_time-start_time))
    return call_func

@set_func  # 等价于 test = set_func(test)
def test(*args, **kwargs): # 有参数无返回值
    print(args, kwargs)
    for i in range(100000):
        pass


if __name__ == '__main__':
    test(1, 2, 3, a=1, b=2)