# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

from urllib import parse

# 将字典转换成url编码的方式
data = {'name': '网络爬虫', 'greet': 'hello world', 'age': 100}
qs = parse.urlencode(data)
print(qs)

# 编码后的url进行解码
result = 'name=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&greet=hello+world&age=100'
print(parse.parse_qs(result))
