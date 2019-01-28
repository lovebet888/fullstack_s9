
'''装饰器的理解'''

# import time
#
# def timeer(func):
#     def inner():
#         start = time.time()
#         func()
#         print(time.time()-start)
#     return inner   #这里返还是inner 不是timeer 否则没有执行内不inner函数
# @timeer
# def func1():
#     time.sleep(0.1)
#     print('in func1')
#
#
# func1()



# import time
# def timer(func):
#     def inner(a):
#         start = time.time()
#         func(a)
#         print(time.time()-start)
#     return inner
# @timer    # func2 = timer(func2)
# def func2(a):
#     time.sleep(0.1)
#     print(a)
# func2(1)

'''装饰器传递一切参数'''
# import time
# def warppers(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         re = func(*args,**kwargs)
#         return re
#     return inner
# @warppers
# def func1(a,b):
#     print('in func1')
#
# @warppers
# def func2(a):
#     print('in func2 and get a {}'.format(a))
#
# func1(2,3)
# func2('aaaa')


def wrapper1(func):
    def inner():
        print('wrapper1 ,before func')
        func()
        print('wrapper1 ,after func')
    return inner

def wrapper2(func):
    def inner():
        print('wrapper2 ,before func')
        func()
        print('wrapper2 ,after func')
    return inner

@wrapper2
@wrapper1
def f():
    print('in f')

f()

'''多个装饰器装饰同一个函数'''





