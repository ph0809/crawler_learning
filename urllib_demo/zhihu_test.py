# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-

from urllib import request
from urllib import parse

result = request.urlopen('https://www.zhihu.com')
print(result.read())
request.urlretrieve('https://www.zhihu.com', 'zhihu.html')