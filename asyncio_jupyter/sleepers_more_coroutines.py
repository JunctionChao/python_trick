#!/usr/bin/env python
# -*- coding: utf-8 -*-


import asyncio
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)


async def sleeper(name, delay, repeat):
    for i in range(1, repeat + 1):
        log.info(f"{name}: START ({i}/{repeat}) wait:{delay}s")
        await asyncio.sleep(delay)
        log.info(f"{name}: END   ({i}/{repeat}) wait:{delay}s")
    return name


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    fut = asyncio.gather(sleeper("A", 6, 1), sleeper("B", 2, 3), sleeper("C", 0.5, 12)) # 并发执行
    log.info("main: START run_until_complete")
    loop.run_until_complete(fut)
    log.info("main: END   run_until_complete")
    print(fut.result())

# 结论：尽管每个协程函数都有阻塞休眠函数，但他们之间并不是阻塞的，而是以一种在效果上类似于多线程的方式协作完成，
# 根据阻塞函数是否完成通过挂起，恢复来协作运行完成

"""
[02:42:41] main: START run_until_complete
[02:42:41] B: START (1/3) wait:2s
[02:42:41] A: START (1/1) wait:6s
[02:42:41] C: START (1/12) wait:0.5s
[02:42:41] C: END   (1/12) wait:0.5s
[02:42:41] C: START (2/12) wait:0.5s
[02:42:42] C: END   (2/12) wait:0.5s
[02:42:42] C: START (3/12) wait:0.5s
[02:42:42] C: END   (3/12) wait:0.5s
[02:42:42] C: START (4/12) wait:0.5s
[02:42:43] B: END   (1/3) wait:2s
[02:42:43] B: START (2/3) wait:2s
[02:42:43] C: END   (4/12) wait:0.5s
[02:42:43] C: START (5/12) wait:0.5s
[02:42:43] C: END   (5/12) wait:0.5s
[02:42:43] C: START (6/12) wait:0.5s
[02:42:44] C: END   (6/12) wait:0.5s
[02:42:44] C: START (7/12) wait:0.5s
[02:42:44] C: END   (7/12) wait:0.5s
[02:42:44] C: START (8/12) wait:0.5s
[02:42:45] B: END   (2/3) wait:2s
[02:42:45] B: START (3/3) wait:2s
[02:42:45] C: END   (8/12) wait:0.5s
[02:42:45] C: START (9/12) wait:0.5s
[02:42:45] C: END   (9/12) wait:0.5s
[02:42:45] C: START (10/12) wait:0.5s
[02:42:46] C: END   (10/12) wait:0.5s
[02:42:46] C: START (11/12) wait:0.5s
[02:42:46] C: END   (11/12) wait:0.5s
[02:42:46] C: START (12/12) wait:0.5s
[02:42:47] A: END   (1/1) wait:6s
[02:42:47] B: END   (3/3) wait:2s
[02:42:47] C: END   (12/12) wait:0.5s
[02:42:47] main: END   run_until_complete
['A', 'B', 'C']
[Finished in 6.3s]
"""