# -*- coding: utf-8 -*-
# -*- author: 彭慧 -*-
from urllib import request

# 将网页上的一个文件保存到本地，baidu.html是文件名
request.urlretrieve("http://www.baidu.com", 'baidu.html')
