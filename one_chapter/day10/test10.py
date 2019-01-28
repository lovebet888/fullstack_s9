# x = 1
# def f(x):
#     print(x)
#
# print(10)

'''函数只是定义不调用内存存储，只有执行函数时候才调用内存'''


# print(globals())
# print(locals())


# def func():
#     a = 12
#     b = 20
#     print(locals())
#     print(globals())
#
# func()

'''作用域'''

# def f1():
#     a = 1
#     def f2():
#         print(a)
#     f2()
# f1()




# def f1():
#     a = 1
#     def f2():
#         def f3():
#             print(a)
#         f3()
#     f2()
#
# f1()





# def f1():
#     a = 1
#     def f2():
#         a = 2
#     f2()
#     print('a in f1 : ',a)
#
# f1()

'''可以理解为两个函数无论是嵌套还是怎么样都是两个内存模块，这样作用域就好理解了'''



# def func():
#     print('in func')
#
# f = func
# print(f)
'''函数名本质是内存地址'''




# def f1():
#     print('f1')
#
#
# def f2():
#     print('f2')
#
#
# def f3():
#     print('f3')
#
# l = [f1,f2,f3]
# d = {'f1':f1,'f2':f2,'f3':f3}
# #调用
# l[0]()
# d['f2']()
'''可以当作容器类型的元素，列表字典都是容器的理解'''

'''
内部函数包含对外部作用域而非全剧作用域名字的引用（全局和外部的区别），该内部函数称为闭包函数
#函数内部定义的函数称为内部函'''

# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     return inner
#
# f = func()
# f()


# 输出--closure--有cell元素，则为闭包函数

def outer():
    name = 'yujun'
    def innner():
        print(name)
        print(innner.__closure__)
    return innner
f = outer()
f()
# 输出--closeure--为none，则不是闭包函数


#
# name = 'yujun'
# def outer():
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
# f = outer()
# f()
'''闭包函数嵌套'''
# def wrapper():
#     money = 1000
#     def func():
#         name = 'yujun'
#         def inner():
#             print(name ,money)
#         return inner
#     return func
# f = wrapper()   #是不是多此一举呢？函数的调用内存模块开始运行，为了返回第二层的嵌套函数内存地址，后面两次调用是嵌套函数的执行
#                 #作用域的扩展
# i = f()
# i()


'''闭包函数获取网络应用'''



# from urllib.request import urlopen
#
# def index():
#     url = "http://www.xiaohua100.cn/index.html"
#     def get():
#         return urlopen(url).read()
#     return get
#
# xiaohua = index()
# content = xiaohua()
# print(content)

#输出的__closure__有cell元素 ：是闭包函数
# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
#
# f = func()
# f()
#
# #输出的__closure__为None ：不是闭包函数
# name = 'egon'
# def func2():
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner
#
# f2 = func2()
# f2()












