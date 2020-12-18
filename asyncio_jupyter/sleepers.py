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
    # https://docs.python.org/3.5/library/asyncio-task.html?highlight=asyncio%20gather#asyncio.gather
    fut = asyncio.gather(sleeper("A", 6, 1))
    log.info("main: START run_until_complete")
    loop.run_until_complete(fut)
    log.info("main: END   run_until_complete")

"""
[02:28:37] main: START run_until_complete
[02:28:37] A: START (1/1) wait:6s
[02:28:43] A: END   (1/1) wait:6s
[02:28:43] main: END   run_until_complete
[Finished in 6.2s]
"""