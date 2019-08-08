''' 多个装饰器装饰一个函数 '''
import os
import time
def wrapper1(func):
    def inner1(*args,**kwargs):
        print("wrapper1,before func")
        ret = func(*args,**kwargs)
        print("wrapper1,after func")
        return ret
    return inner1
def wrapper2(func):
    def inner2(*args,**kwargs):
        print("wrapper2,before func")
        ret = func(*args,**kwargs)
        print("wrapper2,after func")
        return ret
    return inner2
@wrapper1
@wrapper2
def f():
    print('in f')
f()