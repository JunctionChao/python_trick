import time
import threading


def test1():
    for i in range(5):
        print("----test1----%d----" %i)
        time.sleep(1)


def test2():
    for i in range(10):
        print("----test2----%d----" %i)
        time.sleep(1)


# 多个线程执行的顺序是操作系统决定的，主线程如果提前运行完成也会等待子线程结束后再结束
def main():
    t1 = threading.Thread(target=test1) # 如果函数有参数，传入 args=(parms1,...)
    t2 = threading.Thread(target=test2)

    t1.start() # 调用start时线程才开始执行
    t2.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()