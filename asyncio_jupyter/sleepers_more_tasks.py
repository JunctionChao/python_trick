#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 用task方式实现协程效果,更高级的接口
# A Task is a wrapper for a coroutine and a subclass of Future.

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

async def main():
    sleeper1 = loop.create_task(sleeper("A", 6, 1))
    sleeper2 = loop.create_task(sleeper("B", 2, 3))
    sleeper3 = loop.create_task(sleeper("C", 0.5, 12))
    await asyncio.wait([sleeper1, sleeper2, sleeper3])
    return sleeper1, sleeper2, sleeper3


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info("main: START run_until_complete")
    s1, s2, s3 = loop.run_until_complete(main())
    log.info("main: END   run_until_complete")
    print(s1.result(), s2.result(), s3.result())

"""
[21:38:44] main: START run_until_complete
[21:38:44] A: START (1/1) wait:6s
[21:38:44] B: START (1/3) wait:2s
[21:38:44] C: START (1/12) wait:0.5s
[21:38:45] C: END   (1/12) wait:0.5s
[21:38:45] C: START (2/12) wait:0.5s
[21:38:45] C: END   (2/12) wait:0.5s
[21:38:45] C: START (3/12) wait:0.5s
[21:38:46] C: END   (3/12) wait:0.5s
[21:38:46] C: START (4/12) wait:0.5s
[21:38:46] B: END   (1/3) wait:2s
[21:38:46] B: START (2/3) wait:2s
[21:38:46] C: END   (4/12) wait:0.5s
[21:38:46] C: START (5/12) wait:0.5s
[21:38:47] C: END   (5/12) wait:0.5s
[21:38:47] C: START (6/12) wait:0.5s
[21:38:47] C: END   (6/12) wait:0.5s
[21:38:47] C: START (7/12) wait:0.5s
[21:38:48] C: END   (7/12) wait:0.5s
[21:38:48] C: START (8/12) wait:0.5s
[21:38:48] B: END   (2/3) wait:2s
[21:38:48] B: START (3/3) wait:2s
[21:38:48] C: END   (8/12) wait:0.5s
[21:38:48] C: START (9/12) wait:0.5s
[21:38:49] C: END   (9/12) wait:0.5s
[21:38:49] C: START (10/12) wait:0.5s
[21:38:49] C: END   (10/12) wait:0.5s
[21:38:49] C: START (11/12) wait:0.5s
[21:38:50] C: END   (11/12) wait:0.5s
[21:38:50] C: START (12/12) wait:0.5s
[21:38:50] A: END   (1/1) wait:6s
[21:38:50] B: END   (3/3) wait:2s
[21:38:50] C: END   (12/12) wait:0.5s
[21:38:50] main: END   run_until_complete
A B C
[Finished in 6.4s]
"""