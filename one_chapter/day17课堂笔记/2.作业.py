# 3.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
name=['alex','wupeiqi','yuanhao','nezha']
# def func(item):
#     return item+'_sb'
# ret = map(func,name)   #ret是迭代器
# for i in ret:
#     print(i)
# print(list(ret))

# ret = map(lambda item:item+'_sb',name)
# print(list(ret))

# 4.用filter函数处理数字列表，将列表中所有的偶数筛选出来
# num = [1,3,5,6,7,8]
# def func(x):
#     if x%2 == 0:
#         return True
# ret = filter(func,num)  #ret是迭代器
# print(list(ret))
#
# ret = filter(lambda x:x%2 == 0,num)
# ret = filter(lambda x:True if x%2 == 0 else False,num)
# print(list(ret))

# 5.随意写一个20行以上的文件
# 运行程序，先将内容读到内存中，用列表存储。
# 接收用户输入页码，每页5条，仅输出当页的内容

# with open('file',encoding='utf-8') as f:
#     l = f.readlines()
# page_num = int(input('请输入页码 ： '))
# pages,mod = divmod(len(l),5) #求有多少页，有没有剩余的行数
# if mod:           # 如果有剩余的行数，那么页数加一
#     pages += 1    # 一共有多少页
# if page_num > pages or page_num <= 0:   #用户输入的页数大于总数或者小于等于0
#     print('输入有误')
# elif page_num == pages and mod !=0:    #如果用户输入的页码是最后一页，且之前有过剩余行数
#     for i in range(mod):
#         print(l[(page_num-1)*5 +i].strip())  #只输出这一页上剩余的行
# else:
#     for i in range(5):
#         print(l[(page_num-1)*5 +i].strip())  #输出5行

# 6.如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]

# 6.1.计算购买每支股票的总价
# ret = map(lambda dic : {dic['name']:round(dic['shares']*dic['price'],2)},portfolio)
# print(list(ret))

# 6.2.用filter过滤出，单价大于100的股票有哪些
# ret = filter(lambda dic:True if dic['price'] > 100 else False,portfolio)
# print(list(ret))
# ret = filter(lambda dic:dic['price'] > 100,portfolio)
# print(list(ret))

# 每周大作业
# 这一周写得所有博客地址，精确到页的url，至少三篇，内容不限
# 大作业 ： py readme（对作业描述，顺便可以写点儿你想和导员沟通的） 流程图
#
