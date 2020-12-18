#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/arocks/async-await-examples/blob/master/chainer.py

import asyncio
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)


async def grandfather():
    log.info(f"grandfather: START")
    await father()
    log.info(f"grandfather: END")


async def father():
    log.info(f"father: START")
    await child()
    log.info(f"father: END")


async def child():
    log.info(f"child: START")
    await asyncio.sleep(3)
    log.info(f"child: END")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info("main: START run_until_complete")
    loop.run_until_complete(grandfather())
    log.info("main: END   run_until_complete")

# https://docs.python.org/3.5/library/asyncio-task.html?highlight=asyncio%20gather#Sequence%20diagram
# 协程函数链式调用时，事件循环驱动函数链式调用(grandfather->father->child)
# 直到碰到阻塞操作(这里就是sleep()),然后才会将控制返回给事件循环，
# 当阻塞操作完成时，再链式的恢复之前挂起的程序，直到运行结束

"""
[03:02:10] main: START run_until_complete
[03:02:10] grandfather: START
[03:02:10] father: START
[03:02:10] child: START
[03:02:13] child: END
[03:02:13] father: END
[03:02:13] grandfather: END
[03:02:13] main: END   run_until_complete
[Finished in 3.2s]
"""