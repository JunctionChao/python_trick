import time
import multiprocessing
import os

def test1():
    for i in range(5):
        print("----test1----%d----" %i)
        print("----子进程test1, pid=%d----" % os.getpid()) # 获取当前进程号
        time.sleep(1)


def test2():
    for i in range(10):
        print("----test2----%d----" %i)
        print("----子进程test2, pid=%d----" % os.getpid()) # 获取当前进程号
        time.sleep(1)


def main():
    print("----父进程pid=%d----" % os.getpid())

    p1 = multiprocessing.Process(target=test1) # 如果函数有参数，传入 args=(parms1,...)
    p2 = multiprocessing.Process(target=test2)

    p1.start()
    p2.start()


if __name__ == "__main__":
    main()