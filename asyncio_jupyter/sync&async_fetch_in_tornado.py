#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)


from tornado.httpclient import HTTPClient
from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

import asyncio

# 同步方式
def synchronous_fetch(url):
    http_client = HTTPClient()
    try:
        response = http_client.fetch(url)
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body)
        return response.body


# 异步的两种方式.效果相同，写法不同
@gen.coroutine
def fetch_coroutines(url):
    http_client = AsyncHTTPClient()
    try:
        response = yield http_client.fetch(url)
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body)
        # raise gen.Return(response.body)  # python3.3版本后就解决兼容问题(协程中return和yield)，可以用下面的代替
        return response.body


async def fetch_coroutines_same(url):
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch(url)
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body)
        return response.body


if __name__ == "__main__":
    url = ""
    loop = asyncio.get_event_loop()
    fut = asyncio.gather(fetch_coroutines_same(url))
    try:
        loop.run_until_complete(task_obj)
    finally:
        loop.close()
    print(fut.result())