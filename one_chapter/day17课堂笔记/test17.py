'''----------------------------------------------作业----------------------------------------------------------'''
# 3.用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
'''我的默写
name=['alex','wupeiqi','yuanhao','nezha']
new_name = map(lambda l:l+'_sb',name)
print(list(new_name))
'''
# name=['alex','wupeiqi','yuanhao','nezha']
# def func(item):
#     return item+'_sb'
# ret = map(func,name)   #ret是迭代器
# for i in ret:
#     print(i)
# print(list(ret))

# ret = map(lambda item:item+'_sb',name)
# print(list(ret))




# 4.用filter函数处理数字列表，将列表中所有的偶数筛选出来
'''
num = [1,3,5,6,7,8]
num1 = filter(lambda x:x%2==0,num)
for i in num1:
    print(i)
'''

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

'''# filter 执行了filter之后的结果集合 <= 执行之前的个数
        #filter只管筛选，不会改变原来的值
# map 执行前后元素个数不变
      # 值可能发生改变'''

# 5.随意写一个20行以上的文件
# 运行程序，先将内容读到内存中，用列表存储。
# 接收用户输入页码，每页5条，仅输出当页的内容

def out_p(num):
    with open('log17',encoding='utf-8') as f:
        line = f.readline()
        # list(line)
        print(type(line))
        # print(line[5*(num-1):5*num-1])
        # for i in line [5*(num-1):5*num-1]:
        #     print(i.strip())
out_p(3)




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


