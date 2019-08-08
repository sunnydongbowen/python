import os
import time
from functools import wraps
from urllib.request import urlopen

'''
1、编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
2、为上面编写装饰器，实现缓存网页内容的功能
        实现下载的页面存放在文件中,如果文件内有值(文件大小部位0)，就优先从文件中读取网页内容，
'''

def cache(func):
    def inner(*args,**kwargs):
        '''如果不为空，不执行get函数，直接打开已经缓存的文件'''
        if os.path.getsize('C:\PycharmProjects\github\html\webcache.html'):
            with open('C:\PycharmProjects\github\html\webcache.html','rb') as f:
                return f.read()
        # 不为空才走这一步，执行函数
        ret = func(*args,**kwargs)

        with open("C:\PycharmProjects\github\html\webcache.html",'wb') as f:
            f.write(b'******'+ret)
        return ret
    return  inner
@cache
def get(url):
    code = urlopen(url).read()
    return code
ret = get("http://www.baidu.com")
print(ret)

