#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2020-11-15
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

"""
匹配简历中 中英文 本科学位名称的 正则表达式
描述本科学位，一般来说："Bachelor", "本科", 等等
eg（包括但不限于）:
    Bachelor of Business Administration
    BS in Electrical Engineering, 2010
    xxxx大学  金融学本科
    xxxx学院  学士学位
"""

import re

pattern = re.compile(r"(Bachelor|Associate|Degree|B\.?[S,A]\.?).*\n$|.*(学士|本科).*\n$", re.IGNORECASE)



egs = ["B.S. in Electrical Engineering, 2010\n",
        "Bachelor of Arts in English, 2012\n",
        "Associate in Arts\n",
        "Associate Degree\n",
        "degree\n",
        "金融学学士学位\n",
        "金融学本科学位\n"]


result_all = [] 
for eg in egs:
    # result = pattern.findall(eg)
    result = re.match(pattern, eg)
    result_all.append(result)

print(result_all)

ret = re.match(r"Bachelor.*\n$", "bachelor of Arts in English, 2012\n", re.IGNORECASE)
print(ret)

ret = re.match(r"(Bachelor|B\.?[S,A]\.?|Associate).*\n$", "Associate of Arts in English, 2012\n")
print(ret)
ret = re.match(r"(Bachelor|B\.?[S,A]\.?|Associate).*\n$", "B.A. of Arts in English, 2012\n")
print(ret)

ret = re.match(r".*(学士|本科).*\n$", "金融学学士学位\n")
print(ret)