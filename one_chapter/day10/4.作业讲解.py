#2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(l):
#     return l[1::2]  #切片
# print(func([1,2,3,4,5]))

# 3、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。
# def func(x):
#     return len(x)>5
# if func('abcd'):
#     print('长度确实大于5')

# 4、写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l):
#     return l[:2]
#
# print(func([1,2,3,4]))

# 5、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。
# def func(s):   #'skghfoiw8qpeuqkd'
#     dic = {'num':0,'alpha':0,'space':0,'other':0}
#     for i in s:
#         if i.isdigit():
#             dic['num']+=1
#         elif i.isalpha():
#             dic['alpha'] += 1
#         elif i.isspace():
#             dic['space'] += 1
#         else:
#             dic['other'] += 1
#     return dic
# print(func('+0-0skahe817jashf wet1'))

# 6、写函数，检查用户传入的对象（字符串、列表、元组）
# 的每一个元素是否含有空内容，并返回结果。
# def func(x):
#     if type(x) is str and x:  #参数是字符串
#         for i in x:
#             if i == ' ':
#                 return True
#     elif x and type(x) is list or type(x) is tuple: #参数是列表或者元组
#         for i in x:
#             if not i:
#                 return True
#     elif not x:
#         return True
#
# print(func([]))

#7、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
#	dic = {"k1": "v1v1", "k2": [11,22,33,44]}
#	PS:字典中的value只能是字符串或列表
# def func(dic):
#     for k in dic:
#         if len(dic[k]) > 2:
#             dic[k] = dic[k][:2]
#     return dic
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(func(dic))

# 8、写函数，接收两个数字参数，返回比较大的那个数字。
# def func(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(func(1,5))

# def func(a,b):
#     return a if a > b else b
# print(func(5,1))

# 三元运算
# a = 1
# b = 5
# c = a if a>b else b   #三元运算
# print(c)

# 变量 = 条件返回True的结果 if 条件 else 条件返回False的结果
#必须要有结果
#必须要有if和else
#只能是简单的情况

# 9、写函数，用户传入修改的文件名，与要修改的内容，
# 执行函数，完成整个文件的批量修改操作（进阶）。
# def func(filename,old,new):
#     with open(filename, encoding='utf-8') as f, open('%s.bak'%filename, 'w', encoding='utf-8') as f2:
#         for line in f:
#             if old in line:  # 班主任:星儿
#                 line = line.replace(old,new)
#             # 写文件
#             f2.write(line)  # 小护士:金老板
#
#     import os
#     os.remove(filename)  # 删除文件
#     os.rename('%s.bak'%filename, filename)  # 重命名文件


'''我的作业'''
#2、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(*args):
#     l = []
#     for i in range(len(args)):
#         if i %2 == 0:
#             l.append(args[i])
#
#     return l
#
# check_out = func(1,2,3,4,5,6,7,8)
# print(check_out)

'''还是老师用的切片方法最简单 这里有个以为缩进错误不能理解后面在找问题，104行的range不能少否则整数迭代报错，还有6个逗号解释不能在放在行内
否则容易出现indentionerror 缩紧错误
'''

# 3、写函数，判断用户传入的值（字符串、列表、元组）长度是否大于5。
# def len_check(*args):
#     if len(args)>5:
#         print('输入长度大于5',args,'*%s'%len(args))
#     else:print(('输入长度小于5',args,'*%s'%len(args)))
# l = input('请输入：')
# len_check(l)
'''和老师理解的意思不同'''
# 4、写函数，检查传入列表的长度，如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l):
#     if len(l)>2:
#         return l[0:2]
#     else:return l
# print(func([2,3,4,5,6]))

'''注意切片的头尾问题顾头不顾尾这里我自己在整理下切片问题'''

# a = 'ABCDEFGHIJK'
# print(a[0:3])
# print(a[2:5])
# print(a[0:]) #默认到最后
# print(a[0:-1]) # -1 是列表中最后一个元素的索引，但是要满足顾头不顾腚的原则，所以取不到K元素
# print(a[0:5:2]) #加步长
# print(a[-1:-5:-2]) #反向加步长
'''切片左总是起点中间是结束点可以正向也可以反向，记数可以从开始记也可以从结尾记数，总之左面为起点中间为结束点
注意顾头不顾腚原则全部包括则尾巴不记数'''

# 5、写函数，计算传入字符串中【数字】、【字母】、【空格】 以及 【其他】的个数，并返回结果。
# def type_count(s):
#     dic={'number':0,'alpha':0,'tab':0,'others':0}
#     for i in s:
#         if i.isdigit():
#             dic['number']+=1
#             if i.isalpha():
#                 dic['alpha']+=1
#                 if i.isspace():
#                     dic['tab']+=1
#                 else:dic['others']+=1
#     return dic
# print(type_count('shhs787 7 7dhd8#&@7@  34'))
'''if嵌套的逻辑不对，应该用elif，用了嵌套逻辑要梳理好'''

# 6、写函数，检查用户传入的对象（字符串、列表、元组）
# 的每一个元素是否含有空内容，并返回结果。
#
# def func(l):
#     num = 0
#     for i in l:
#         if i.isspace():
#             num+=1
#     if num == 0:
#         print('输入正确')
#     else:print('输入%s空格'%num)
# func(['3','a',''])
'''理解有误是空内容不是空格'''
# def check(x):
#     if type(x) is str and x:  #参数是字符串
#         for i in x:
#             if i == ' ':
#                 return True
#     elif type(x) is list or type(x) is tuple: #参数是列表或者元祖
#         for i in x:
#             if not i:
#                 return True
#     elif not x:
#         return True
# print(check('dhhd'))
'''题目和逻辑不对'''

#7、写函数，检查传入字典的每一个value的长度,如果大于2，
# 那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(dic):
#     for i,v in dic.items():
#         if len(v) > 2:
#             dic[i] = v[:2]
#     return dic
# print(func({'name1':'ac','name2':'dfree','name3':'fgc'}))


#
# dic = {"name":"jin","age":18,"sex":"male"}
# for key in dic:
#     print(key)
# for item in dic.items():
#     print(item,type(item))
# for key,value in dic.items():
#     print(key,value)

'''注意字典的遍历第一部分的基础不是很牢固今晚把它梳理一遍做作业就是查漏补缺'''

# 8、写函数，接收两个数字参数，返回比较大的那个数字。
def func(a,b):
    # if a>b:
    #     return a
    # else: return b
    return a if a>b else b

print(func(2,3))


# 9、写函数，用户传入修改的文件名，与要修改的内容，
# 执行函数，完成整个文件的批量修改操作（进阶）。

def file_update(filename):
    with open('filename',mode='w+',encoding='utf-8') as f:
        line = f.readline()
        for i in line:
            if i == 'e':
                i = 'love'
    return line
filter('log10')




