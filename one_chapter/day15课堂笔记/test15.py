'''作业'''
# 3.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕
# f = open('inputfile',encoding='utf-8')\
#     line = f.readline()
#     def tail():
#         if like in line:
#             yield line
# print(i for i in line)


# 4.写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。

# def check_file(filename):
#     with open(filename,encoding='utf-8') as f:
#         for i in f:
#             yield '***'+i
# for i in check_file('1.复习.py'):
#     print(i.strip())

# def check_file(filename):
#     with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
#         for i in f:
#             yield '***'+i
#
# for i in check_file(''):
#     print(i.strip())
'''-------------------------------------------第二次作业默写------------------------------------------'''
# 3.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕

'''还是要注意while的位置
def generator(filename,aim):    #注意传两个参数
    with open(filename,encoding='utf8') as f:
        while True:            这里也可以用for读取和while一个逻辑
            line = f.readline()
            if 'love' in line:
                yield line
g = generator('log15','love')
for i in g:
    print(i)
'''


# def check_file(filename,aim):
#     with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
#         for i in f:
#             if aim in i:
#                 yield i
#
# g = check_file('1.复习.py','生成器')
# for i in g:
#     print(i.strip())


# 4.写生成器，从文件中读取内容，在每一次读取到的内容之前加上‘***’之后再返回给用户。
''''我的默写
def generator(filename):
    with open(filename,encoding='utf-8') as f:
        for i in f:
            yield '***'+i
gen1 = generator('log15')
for i in gen1:
    print(i)
'''

# def check_file(filename):
#     with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
#         for i in f:
#             yield '***'+i
#
# for i in check_file('1.复习.py'):
#     print(i.strip())


