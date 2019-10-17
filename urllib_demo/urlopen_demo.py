# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-
from urllib import request

# 通过下面三行代码可以将百度首页的所有内容爬下来
resp = request.urlopen('http://www.baidu.com')
print(resp.read())

