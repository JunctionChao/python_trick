#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

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
    tasks = []
    for t in (("A", 6, 1), ("B", 2, 3), ("C", 0.5, 12)):
        task = asyncio.ensure_future(sleeper(*t))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info("main: START run_until_complete")
    fut = loop.run_until_complete(main())
    log.info("main: END   run_until_complete")
    print(fut)

"""
[16:20:15] main: START run_until_complete
[16:20:15] A: START (1/1) wait:6s
[16:20:15] B: START (1/3) wait:2s
[16:20:15] C: START (1/12) wait:0.5s
[16:20:15] C: END   (1/12) wait:0.5s
[16:20:15] C: START (2/12) wait:0.5s
[16:20:16] C: END   (2/12) wait:0.5s
[16:20:16] C: START (3/12) wait:0.5s
[16:20:16] C: END   (3/12) wait:0.5s
[16:20:16] C: START (4/12) wait:0.5s
[16:20:17] B: END   (1/3) wait:2s
[16:20:17] B: START (2/3) wait:2s
[16:20:17] C: END   (4/12) wait:0.5s
[16:20:17] C: START (5/12) wait:0.5s
[16:20:17] C: END   (5/12) wait:0.5s
[16:20:17] C: START (6/12) wait:0.5s
[16:20:18] C: END   (6/12) wait:0.5s
[16:20:18] C: START (7/12) wait:0.5s
[16:20:18] C: END   (7/12) wait:0.5s
[16:20:18] C: START (8/12) wait:0.5s
[16:20:19] B: END   (2/3) wait:2s
[16:20:19] B: START (3/3) wait:2s
[16:20:19] C: END   (8/12) wait:0.5s
[16:20:19] C: START (9/12) wait:0.5s
[16:20:19] C: END   (9/12) wait:0.5s
[16:20:19] C: START (10/12) wait:0.5s
[16:20:20] C: END   (10/12) wait:0.5s
[16:20:20] C: START (11/12) wait:0.5s
[16:20:20] C: END   (11/12) wait:0.5s
[16:20:20] C: START (12/12) wait:0.5s
[16:20:21] A: END   (1/1) wait:6s
[16:20:21] B: END   (3/3) wait:2s
[16:20:21] C: END   (12/12) wait:0.5s
[16:20:21] main: END   run_until_complete
['A', 'B', 'C']
"""