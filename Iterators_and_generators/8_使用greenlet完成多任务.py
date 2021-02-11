# greenlet对yield进行了封装，耗时操作还是会等待
from greenlet import greenlet
import time


def test1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---b---")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()