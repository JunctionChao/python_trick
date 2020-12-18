#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-07
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from pprint import pprint

async def hi():
    print("HOWDY")


import asyncio
loop = asyncio.get_event_loop()
print(loop) # <_WindowsSelectorEventLoop running=False closed=False debug=False>
o = hi()
loop.run_until_complete(o)
pprint(dir())