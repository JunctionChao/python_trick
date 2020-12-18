#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://docs.python.org/3.5/library/asyncio-task.html#asyncio.coroutine
# 使用 @asyncio.coroutine装饰器 装饰基于生成器写法 的协程，可以互相兼容
# This enables the generator use yield from to call async def coroutines, 
# and also enables the generator to be called by async def coroutines, for instance using an await expression.

"""
yield from 结构会在内部自动捕获StopIteration 异常。
这种处理方式与 for 循环处理 StopIteration异常的方式一样：循环机制使用用户易于理解的方式处理异常。
对yield from 结构来说，解释器不仅会捕获 StopIteration 异常，还
会把 value 属性的值变成 yield from 表达式的值
"""
# https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/

import asyncio
import logging


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

@asyncio.coroutine
def grandfather():
    log.info(f"grandfather: START")
    yield from father()
    log.info(f"grandfather: END")


async def father():
    log.info(f"father: START")
    await child()
    log.info(f"father: END")


@asyncio.coroutine
def child():
    log.info(f"child: START")
    yield from asyncio.sleep(3)
    log.info(f"child: END")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    log.info("main: START run_until_complete")
    loop.run_until_complete(grandfather())
    log.info("main: END   run_until_complete")

"""
[14:34:06] main: START run_until_complete
[14:34:06] grandfather: START
[14:34:06] father: START
[14:34:06] child: START
[14:34:09] child: END
[14:34:09] father: END
[14:34:09] grandfather: END
[14:34:09] main: END   run_until_complete
[Finished in 3.2s]
"""