from multiprocessing import Pool
import os, time, random

def worker(msg):
    start = time.time()
    print("%s 开始执行，进程号为 %d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    stop = time.time()
    print(msg, " 执行完毕，耗时 %0.2f" % (stop-start))


if __name__ == "__main__":
    po = Pool(4) # 定义最大进程数为4的进程池
    for i in range(10):
        po.apply_async(worker, (i,))

    print("---start---")
    po.close() # 关闭进程池，关闭后po不再接受新的请求
    po.join() # 等待po中所有子进程执行完成，必须放在close之后
    print("---end---")