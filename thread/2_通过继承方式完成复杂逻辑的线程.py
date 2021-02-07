import time
import threading


class MyThread1(threading.Thread):
    def run(self):
        for i in range(5):
            print("----MyThread1----%d----" %i)
            time.sleep(1)


class MyThread2(threading.Thread):
    def run(self):
        for i in range(10):
            print("----MyThread2----%d----" %i)
            time.sleep(1)


def main():
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()