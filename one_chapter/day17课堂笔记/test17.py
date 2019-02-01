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
'''逻辑功能太简单没有用到内置函数
def out_p(num):
    with open('log17',encoding='utf-8') as f:
        line = f.readline()
        # list(line)
        print(type(line))
        # print(line[5*(num-1):5*num-1])
        # for i in line [5*(num-1):5*num-1]:
        #     print(i.strip())
out_p(3)
'''



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


'''---------------------------------二分查找法------------------------------------------'''
'''逻辑需要再次明确

l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
def find(l,aim,start=0,end=None):
    end = len(l) if end is None else end
   #少一个start，没有考虑从整个l出发
    mid_index = (end-start)//2+start
    #卡住了怎么把开始和结束传到这个函数,定义一个中间变量好想法我没想到,最外层少了一个if else
    if start<= end:
        if aim > l[mid_index]:
                return find(l,aim,start = mid_index+1,end=end)
        elif aim<l[mid_index]:
                return find(l,aim,start=start,end=mid_index-1)
        #这里else返回mid_index
        else:
                return mid_index
    else:
         return '找不到'


ret = find(l,44)
print(ret)
'''


#正确的

# def find(l,aim,start = 0,end = None):
#     end = len(l) if end is None else end
#     mid_index = (end - start)//2 + start
#     if start <= end:
#         if l[mid_index] < aim:
#             return find(l,aim,start =mid_index+1,end=end)
#         elif l[mid_index] > aim:
#             return find(l, aim, start=start, end=mid_index-1)
#         else:
#             return mid_index
#     else:
#         return '找不到这个值'
#
#
# ret= find(l,44)
# print(ret)

'''--------------------------------------------递归函数与三级菜单--------------------------------------'''

menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

def threeLM(dic):
    while True:
        for k in dic:print(k)
        key = input('input>>').strip()
        if key == 'b' or key == 'q':return key
        elif key in dic.keys() and dic[key]:
            ret = threeLM(dic[key])
            if ret == 'q': return 'q'

threeLM(menu)

'''逻辑问题'''