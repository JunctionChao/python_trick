# 使用gevent，程序遇到耗时操作则会自动切换任务，不会浪费时间等待

import gevent
import time
from gevent import monkey
# 打补丁，不需要改原来的耗时操作，否则是要使用gevent提供的模块
monkey.patch_all()
def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # 不打补丁则使用gevent提供的耗时模块
        # gevent.sleep(0.5)
        time.sleep(0.5)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
# g1.join()
# g2.join()
# g3.join()
# 一次性添加全部的任务
gevent.joinall([g1,g2,g3])