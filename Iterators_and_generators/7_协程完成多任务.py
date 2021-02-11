import time
# 虽然是多任务但是耗时操作还是会等待
def test1():
    while True:
        print("--1--")
        time.sleep(0.5)
        yield

def test2():
    while True:
        print("--2--")
        time.sleep(0.5)
        yield

if __name__ == "__main__":
        t1 = test1()
        t2 = test2()
        while True:
                next(t1)
                next(t2)