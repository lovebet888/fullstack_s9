# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
#
# print(list(g))
# print(list(g1))
# print(list(g2))

# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# # for n in [1,10,5]:
# #     g=(add(n,i) for i in g)
# n = 1
# g=(add(n,i) for i in test())
# n = 10
# g=(add(n,i) for i in (add(n,i) for i in test()))
# n = 5
# g=(15,16,17,18)


# print(list(g))


'''生成器表达式和生成器不调用 就不执行 直到最后调用 理解好上面面试题就简单了'''
'''如期数据类型一个改变全局变，类似于赋值地址的逻辑'''

'''这个题目的输出结果好好体会list是默认参数那么默认参数的陷进和注意事项要注意'''
# def extand_list(val,list=[]):
#     list.append(val)
#     return list
# list1 = extand_list(10)
# list2 = extand_list(123,[])
# list3 = extand_list('a')
# list4 = extand_list('b')
# list5 = extand_list(345,[])
# print('list1 = %s'%list1)
# print('list2 = %s'%list2)
# print('list3 = %s'%list3)
# print('list4 = %s'%list4)
# print('list5 = %s'%list5)


'''-----------------------------------第二次理解面试题目-----------------------------------------'''
#体会输出结果

# def demo():
#     for i in range(4):
#         yield i
#
# g=demo()
#
# g1=(i for i in g)
# g2=(i for i in g1)
# '''到这里所有的函数都没有执行只是定义，生成器表达式理解为定义生成器不做任何函数运算直到list才运行，当本次list执行完生成器里面的值全部释放
# 为空了，所以接下来在找它调用已经是空的，所以打印出来是空的'''
# print(list(g))
# print(list(g1))
# print(list(g2))



#面试题 二

# def add(n,i):
#     return n+i
#
# def test():
#     for i in range(4):
#         yield i
#
# g=test()
# # for n in [1,10]:
# #     g=(add(n,i) for i in g)
# '''上面两行代码可以理解为'''
# n = 1
# g = add(1,i) for i in g
# n = 10
# g = add(10,i) for i in g   #这里的 i in g 中的g 是上一个for循环n=1后面的g赋值这下就明白了
#
#                 # g = add(10,i) for i in g=add(10,i) for i in test()///////函数是有在list后才开始运行其他时间只是定义
# '''到这里g也没有运算，生成器和生成器表达式不找它要值就不运算，节省内存'''
# print(list(g))


#面试题二拓展

# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g = test()
# for n in [1,10,5]:
#     g = (add(n,i) for i in g)    #这里的g就是循环的取上面的g，这里的g也是生成器表达式，可以迭代挨个取
# print(list(g))








