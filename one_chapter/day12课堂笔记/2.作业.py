# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
# FLAG = False
# def login(func):
#     def inner(*args,**kwargs):
#         global FLAG
#         '''登录程序'''
#         if FLAG:
#             ret = func(*args, **kwargs)  # func是被装饰的函数
#             return ret
#         else:
#             username = input('username : ')
#             password = input('password : ')
#             if username == 'boss_gold' and password == '22222':
#                 FLAG = True
#                 ret = func(*args,**kwargs)      #func是被装饰的函数
#                 return ret
#             else:
#                 print('登录失败')
#     return inner
#
# @login
# def shoplist_add():
#     print('增加一件物品')
#
# @login
# def shoplist_del():
#     print('删除一件物品')
#
# shoplist_add()
# shoplist_del()

# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
# def inputfile(func):
#     def inner(*args,**kwargs):
#         with open('inputfile','a',encoding='utf-8') as f:
#             f.write(func.__name__+'\n')
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @inputfile
# def shoplist_add():
#     print('增加一件物品')
#
# @inputfile
# def shoplist_del():
#     print('删除一件物品')
#
# shoplist_add()
# shoplist_del()
# shoplist_del()
# shoplist_del()
# shoplist_del()
# shoplist_del()

# 进阶作业(选做)：
# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中
# import os
# from urllib.request import urlopen
# def cache(func):
#     def inner(*args,**kwargs):
#         if os.path.getsize('web_cache'):
#             with open('web_cache','rb') as f:
#                 return f.read()
#         ret = func(*args,**kwargs)  #get()
#         with open('web_cache','wb') as f:
#             f.write(b'*********'+ret)
#         return ret
#     return inner
#
# @cache
# def get(url):
#     code = urlopen(url).read()
#     return code


# {'网址':"文件名"}
# ret = get('http://www.baidu.com')
# print(ret)
# ret = get('http://www.baidu.com')
# print(ret)
# ret = get('http://www.baidu.com')
# print(ret)



'''我的作业'''

#1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名
'''逻辑上不对特别是flag的理解'''
# flag = False
# while not flag:
#     def warppers(func):
#         global flag
#         def inner(*args,**kwargs):
#             '''先读取文件生成字典'''
#             dic = {}
#             with open('log12',encoding='utf-8') as f:
#                 while True:
#                     line = f.readline()
#                     if not line:
#                         break
#                     dic.setdefault(line.split()[0],line.split()[1])
#             '''输入用户名密码并验证是否正确'''
#             username = input("请输入用户名：")
#             password = input('请输入密码：')
#             if username in dic.keys():
#                 for i in dic.keys:
#                     if username == i and password == dic[i]:
#                         print('输入正确')
#                     else:
#                         print('用户名或者密码错误')
#                         flag = True
#             else:
#                 print('输入用户名或者密码错误')
#                         flag = True
#             ret =  func(*args,**kwargs)
#             return ret
#         return inner
# @warppers
# def func():

'''再次整理下思路重新写一遍'''
# flag = False
# def login_func(func):
#     def inner(*args,**kwargs):
#         global flag
#         '''登陆程序'''
#         if flag:
#             re = func(*args,**kwargs)
#             return re
#         else:
#             username =  input('请输入用户名：')
#             password = input('请输入密码：')
#             if username =='ang cui' and password == 'test123':
#                 print('登陆成功')
#                 re = func(*args,**kwargs)
#                 flag = True
#                 return re
#             else:
#                 print('你的用户名或者密码错误')
#
#     return inner
# @login_func
# def shop_add():
#     print('你增加了一件商品')
# @login_func
# def shop_del():
#     print('你删除了一件商品')
#
#
# shop_del()
# shop_del()
#




'''读取文件生成字典的测试'''
# with open('log12', encoding='utf-8') as f:
#     dic = {}
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         else:
#             dic.setdefault(line.split()[0],line.split()[1])
#     print(dic)

'''打开文件readline 逐行读，readlines一次性读完,readline返回字符串 readlines返回是以行为单元的列表,切片有返回值直接可以print'''


# 2.编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
def warppers(func):
    def inner(*args,**kwargs):
        with open('login_details','r',encoding='utf-8') as f:
            f.write(func.__name__+'\n')
        ret = func(*args,**kwargs)
        return ret
    return inner
@warppers
def func1():
    print('1')
@warppers
def func2():
    print('2')
func1()
func1()
func1()




'''write没有返回值，而且名字方法得自己写出来,读写模式mode可以不写直接写句柄，w或者w+有则清空在写入，a模式为有内容只追加模式不可读
r+模式也是有则清空在继续写入'''
