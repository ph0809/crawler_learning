# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-
from urllib import parse, request

url = "http://www.baidu.com/s?username=zhiliao"

result = parse.urlsplit(url)
# result = parse.urlparse(url)   # 多了一个params属性
print(result)
