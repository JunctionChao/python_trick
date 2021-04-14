import time
import threading


def test1():
    for i in range(5):
        print("----test1----%d----" %i)
        time.sleep(1)
    print("子线程test1结束")


def test2():
    for i in range(10):
        print("----test2----%d----" %i)
        time.sleep(1)
    print("子线程test2结束")


# 多个线程执行的顺序是操作系统决定的
def main():
    t1 = threading.Thread(target=test1) # 如果函数有参数，传入 args=(parms1,...)
    t2 = threading.Thread(target=test2)

    t1.start() # 调用start时线程才开始执行
    t2.start()

    # t1.join()
    # t2.join() # 这里主线程调用某个子线程的join()方法，会阻塞当前主线程直到子线程运行完毕
    # print(threading.enumerate())

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()
    print("主线程结束")
