import time

def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('函数 {} ran in: {} sec'.format(func.__name__, stop_time-start_time))
    return call_func

@set_func  # 等价于 test = set_func(test)
def test(): # 无参数无返回值
    for i in range(100000):
        pass


if __name__ == '__main__':
    test()