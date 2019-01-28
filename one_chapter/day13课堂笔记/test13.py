





'''微博面试题要体会好'''
# def demo():
#     for i in range(4):
#         yield i
# g = demo()
# g1 = (i for i in g)
# g2 = (i for i in g1)
# print(list(g1))
# print(list(g2))
#
#
#
#
# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
#
# print(list(g))


'''自己写的监听文件输入while用的位置不对'''
# def tail(filename):
#     while True:
#             with open(filename,encoding='utf-8') as f:
#                 line = f.readline()
#                 if line:
#                     yield line.strip()
# g=tail('inputfile')
# # print(g)
#
# for i in g:
#     print(i)

# def tail(filename):
#     f=open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line:
#             yield line.strip()
# g = tail('log13')
# # print(g)    g为一个生成器 虽然有返回值但是不会执行内部函数，和return 不同return直接是结束函数 yield 不是
# for i in g:
#     print(i)

'''为什么以上代码不能实时监听？类似视频中的代码可以实时监听文件的'''


'''微博的总结'''
'''默写'''
# import time
# def genrator_fun1():
#     a = 1
#     print('现在定义了a变量')
#     yield a
#     b = 2
#     print('现在又定义了b变量')
#     yield b
# g1 = genrator_fun1()
# print('g1 : ',g1)       #打印g1可以发现g1就是一个生成器
# print('-'*20)   #我是华丽的分割线
# print(next(g1))
# time.sleep(1)   #sleep一秒看清执行过程
# print(next(g1))




'''默写'''
# import time
# def generator_func1():
#     a = 1
#     print('现在定义变量a')
#     yield a
#     b = 2
#     print('现在定义变量b')
#     yield b
# g1 = generator_func1()
# print('g1:',g1)
# print('--'*6)
# print(g1.__next__())
# time.sleep(1)
# print(g1.__next__())
# '''这里可以理解函数调用完的释放 return 和yield'''
# print(generator_func1().__next__())
# time.sleep(1)
# print(generator_func1().__next__())


# def produce():
#     '''生成衣服'''
#     for i in range(25000):
#         yield i
# func1 = produce()
# print(func1.__next__())
# print(func1.__next__())
# print(func1.__next__())
# sum = 0
# for i in func1:
#     sum += 1
#     print(i)
#     if sum == 5:
#         break


# def generator():
#     print(123)
#     content = yield 1
#     print('======',content)
#     print(456)
#     content = yield 2
# func1 = generator()
# ret =func1.__next__()
# print('****',ret)
# ret =generator().send('hello')  #理解这里generator 和 func1的区别
# print('******',ret)



# def generator():
#     print(123)
#     content = yield 1
#     print('=======',content)
#     print(456)
#     yield 2
#
# g = generator()
# ret = g.__next__()
# print('***',ret)
# ret = g.send('hello')   #send的效果和next一样
# print('***',ret)

#send 获取下一个值的效果和next基本一致
#只是在获取下一个值的时候，给上一yield的位置传递一个数据
#使用send的注意事项
# 第一次使用生成器的时候 是用next获取下一个值
# 最后一个yield不能接受外部的值




'''我默写的移动平均值
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        item = yield average
        count += 1
        total += item
        average = total/count
        return average
g_average = averager()
next(g_average)
g_average.send(10)
g_average.send(20)
g_average.send(30)

逻辑问题 为什么是yield average 不是total 也不需要返回值因为yield已经和return功能一样
'''

'''正确的'''
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield average
#         total += term
#         count += 1
#         average = total/count
#
#
# g_avg = averager()
# #next(g_avg)   #和下面的next方法一样
# g_avg.__next__()
# print(g_avg.send(10))
# print(g_avg.send(30))
# print(g_avg.send(5))

'''默写yield from 用法
#
# def gen1():
#     for c in 'ab':
#         yield c
#     for d in '123':
#         yield d
# get_gen = gen1()
# #print(get_gen)   #有yeild返回值但是只有next调用才可以，yield是生成器的标志但是要使用必须配合netx或者send
# print(get_gen.__next__())  #和函数不同，函数可以直接返回值直接打印，生成器返回是一个迭代对象不可以直接打印，好好体会下面正确的
                             #用的list，而我直接用next方法只可以调用一次迭代对想

# def func():
#     return 2
# func1 = func()
# print(func1)

def gen1():
    yield from 'ab'
    yield from '123'
print(list(gen1()))

'''

'''正确的'''

# def gen1():
#     for c in 'AB':
#         yield c
#     for i in range(3):
#         yield i

# print(list(gen1()))

# def gen2():
#     yield from 'AB'
#     yield from range(3)
#
# print(list(gen2()))



'''突然想到split和join方法研究下

# l= 'eerr  6677    hj   6'
# s = l.split()
# print(s)


str = "-"
seq = ("a", "b", "c") # 字符串序列
print (str.join(seq))



l= 'eerr  6677    hj   6'
s = l.split('e')
print(s)
'''


'''默写复习------------------------------------------------------------------------------------------------------'''

#基础装饰器 为了在没有装饰器时候函数正常运行

'''默写
from functools import wraps
def wrapper(func):
    @wraps()   #这里少被装饰函数
    def inner(*args,**kwargs):
        re = func(*args,**kwargs)
        return re
    return inner

@wrapper
def func():
    pass
func()
'''

'''正确的'''


# from functools import wraps
        # def wrapper(func):
        #     @wraps(func)
        #     def inner(*args,**kwargs):
        #          '''在函数被调用之前添加的代码'''
        #         ret = func(*args,**kwargs)   # func是被装饰的函数 在这里被调用
        #         '''在函数被调用之后添加的代码'''
        #         return ret
        #     return inner
        # 使用 —— @wrapper
        # @wrapper
        # def func():   #inner
        #     pass
        #
        # func.__name__


#带参数的装饰器为了多个参数被装饰一键关闭这个装饰器
'''
Flag = True
def wra_out(flag)
    if flag:
        def wrapper(func):
            def inner(*args,**kwargs):
                re =  func(*args,**kwargs)
                return re
            return inner
    return wra_out

@wra_out(Flag)

def func1():
    pass
'''

'''正确'''


# @wrapper -- > @warapper(argument)
        # 三层嵌套函数
        # def outer(形参):
        #     def wrapper(func):
        #         def inner(*args,**kwargs):
        #             '''在函数被调用之前添加的代码'''
        #             ret = func(*args,**kwargs)   # func是被装饰的函数 在这里被调用
        #             '''在函数被调用之后添加的代码'''
        #             return ret
        #         return inner
        #     return wrapper
        # @outer(True)
        # def func():
        #     pass


'''上节课带参数的装饰器源码'''

# import time
# FLAGE = True
# def timmer_out(flag):
#     def timmer(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 start = time.time()
#                 ret = func(*args,**kwargs)
#                 end = time.time()
#                 print(end-start)
#                 return ret
#             else:
#                 ret = func(*args, **kwargs)
#                 return ret
#         return inner
#     return timmer
# # timmer = timmer_out(FLAGE)
# @timmer_out(FLAGE)    #wahaha = timmer(wahaha)
# def wahaha():
#     time.sleep(0.1)
#     print('wahahahahahaha')
#
# @timmer_out(FLAGE)
# def erguotou():
#     time.sleep(0.1)
#     print('erguotoutoutou')
#
# wahaha()
# erguotou()



#多个装饰器装饰一个函数要知道运行结果



# def wrapper1(func):
#     def inner1():
#         print('wrapper1 ,before func')
#         ret = func()
#         print('wrapper1 ,after func')
#         return ret
#     return inner1
#
# def wrapper2(func):
#     def inner2():
#         print('wrapper2 ,before func')
#         ret = func()
#         print('wrapper2 ,after func')
#         return ret
#     return inner2
#
# def wrapper3(func):
#     def inner3():
#         print('wrapper3 ,before func')
#         ret = func()
#         print('wrapper3 ,after func')
#         return ret
#     return inner3
#
# @wrapper3
# @wrapper2
# @wrapper1
# def f():
#     print('in f')
#     return '哈哈哈'
#
# print(f())

'''监听文件输入默写

def tail(filename):
    with open(filename,encoding='utf8') as f:
        # line = f.readline()   #while true 位置不同会引起的反应不同，我的默写就时一直输出第一行.我的写法导致yiled一直运行死循环了
        # while True:
        while True:
            line = f.readline()
            if line:     #逻辑的使用的，line空的时false有内容时true
                yield line.strip()
#print(list(tail('log13')))      #这里卡住了，怎么才能让他实时的去写呢，和输入文件同步？我没有想到for****
g = tail('log13')
for i in g:
    print(i)

'''


#————————————————正确————————————————————————

# def tail(filename):
#     f = open(filename,encoding='utf-8')
#     while True:
#         line = f.readline()
#         if line.strip():
#             yield line.strip()
#
# g = tail('file')
# for i in g:
#     # if 'python' in :
#     #     print('***',i)
#     print(i)






