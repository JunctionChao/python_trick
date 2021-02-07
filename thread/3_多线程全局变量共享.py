"""
在一个函数中对全局变量修改时，是否需要使用global，取决于是否对全局变量的执行指向进行了修改
如果修改了指向，即全局变量指向了一个新的地址，则必须使用global，例如普通的数值型，字符串， list1 += [1,2](修改了list1的指向)
如果只是修改了指向地址中的数据，则不需要使用global，例如 list1.append(3)
"""

import threading, time


def test1(temp):
    temp.append(3)
    print("---in test1 temp=%s---" % str(temp))

def test2(temp):
    print("---in test1 temp=%s---" % str(temp))

nums = [1, 2]

# 多线程之间全局变量共享
def main():
    t1 = threading.Thread(target=test1, args=(nums,)) # 第二个参数为元组
    t2 = threading.Thread(target=test2, args=(nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("---in main Thread nums=%s---" % str(nums))


if __name__ == "__main__":
    main()