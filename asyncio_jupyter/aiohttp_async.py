#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from aiohttp import ClientSession


tasks = []
url = "https://www.baidu.com/"
async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            print(response)
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            html = await response.read()
            print(html.decode('utf-8'))

            html = await response.text()
            print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))