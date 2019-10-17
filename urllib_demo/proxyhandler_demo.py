# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-
from urllib import request

# 没有使用代理
# res = request.urlopen('http://httpbin.org/get')
# print(res.read().decode('utf-8'))

# 使用了代理
handler = request.ProxyHandler({'http': '218.66.161.88:31769'})
opener = request.build_opener(handler)
req = request.Request('http://httpbin.org/ip')
resp = opener.open(req)
print(resp.read())
