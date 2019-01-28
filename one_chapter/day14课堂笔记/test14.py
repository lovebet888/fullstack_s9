# def generator():
#     print('***123')
#     yield 1
#     print('@@@@234')
#     yield 2
#     print('!!!345')
# g=generator()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

'''---------------------------------------移动平均值---------------------------------------'''
# def average():
#     count = 0
#     sum = 0
#     avg = 0
#     while True:
#         num = yield avg
#         count += 1
#         sum += num
#         avg = sum/count
# ave_g = average()
# ave_g.__next__()
# av1 = ave_g.send(5)
# av1 = ave_g.send(10)
# print(av1)


'''---------------------------------------复习-------------------------------------------'''

#从生成器中取值的几个方法
# next
# for
# 数据类型的强制转换 : 占用内存




'''---------------------------------------面试题------------------------------------'''

# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g1))
# print(list(g2))


'''---------------------------------预激生成器的装饰器--------------------------------------
#就是用了一个装饰器扮演生成器的next方法

'''我的默写就以移动平均值为例'''


def warpper(func):
    def inner(*args,**kwargs):
        re = func(*args,**kwargs)
        #func().__next__()  func()错误 func错误 都是被修饰函数之后发生的事情为什么非得时re才可以？暂时理解为返回的是re，如果是func操作
        func().__next__()  #装饰器返回值不是原函数的.next方法
        return re
    return inner

@warpper
def averager():
    total = 0.0
    count = 0
    average = 0
    while True:
        item = yield average
        total += item
        count += 1
        average = total/count

g = averager()

print(g.send(10))
print(g.send(20))
print(g.send(30))


# def gen1():
#     yield 2
# print(gen1().__next__())
#
# g1 = gen1()
# print(gen1().__next__())
'''

#预激生成器的装饰器
# def init(func):   #装饰器
#     def inner(*args,**kwargs):
#         g = func(*args,**kwargs)    #g = average()
#         g.__next__()
#         return g
#     return inner
#
# @init
# def average():
#     sum = 0
#     count = 0
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num    # 10
#         count += 1    # 1
#         avg = sum/count
#
# avg_g = average()   #===> inner
# ret = avg_g.send(10)
# print(ret)
# ret = avg_g.send(20)
# print(ret)




