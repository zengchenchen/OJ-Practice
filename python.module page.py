from urllib.request import *
with urlopen('https://www.douban.com') as f:
    context = f.read()
    print(context[:50])

from urllib import request  # from urllib import * 错误
with request.urlopen('https://www.douban.com') as f:
    context = f.read()
    print(context[:50])

import urllib.request as t  # 用t来作为模块urllib.request的别名, 若没有as则报错
with t.urlopen('https://www.douban.com') as f:
    context = f.read()
    print(context[:50])

# from urllib import * 错误
# with request.urlopen('https://www.douban.com') as f:
#     context=f.read()
#     print(context[:50])

# urllib是包，一堆module的集合，也是一堆.py文件
