"""
多线程共享全局变量，导致全局变量修改出错的原因是操作的非原子性
解决方案：互斥锁解决资源竞争问题

死锁：
在线程之间共享多个资源时，如果两个线程分别战友一部分资源并且同时等待对方的资源就会造成死锁
解决方案：1.添加超时时间 2.程序设计尽量避免(银行家算法)
"""

import threading, time


g_num = 0

def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 上锁
        g_num += 1
        mutex.release() # 释放锁
    print("---in test1 g_num=%d---" % g_num)

def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire() # 上锁
        g_num += 1
        mutex.release() # 释放锁
    print("---in test2 g_num=%d---" % g_num)


# 创建一个互斥锁
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1, args=(10000,))
    t2 = threading.Thread(target=test1, args=(10000,))

    t1.start()
    t2.start()

    time.sleep(3)
    print("---in main Thread g_num=%d---" % g_num)


if __name__ == "__main__":
    main()