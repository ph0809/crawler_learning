# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}
req = request.Request('http://www.baidu.com', headers=headers)
resp = request.urlopen(req)
print(resp.read())
