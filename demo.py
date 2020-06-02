# print("hello word!")   #字符串
# print(2333) #整数
# print(2.333)   #小数
# print(None)  #
# print(True,False)  #布尔值
# print(())    #元组
# print({})   #字典
# print([])   #数组

# a = "哈哈哈"   #把哈哈哈这个值赋值给变量a
# print(a)   #变量不用加引号

# name ="张三"
# print("你好,{}".format(name))
# #这就是单行注释
# """
# 这是多行注释
# #数据十一号
# """
# print("1,"+"1")
# print(1+1)
# print((((2+1)*10)/3)-7)
# print(2>1)
# name = input("请输入你的姓名：")
# print("这是input获取的值："，name)

# #通过input获取两个数字，并计算他们的和
# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# c = (a+b)
# print("两数字之和："，c)

# #请实现一个数数字的功能
# a = input("请输入内容：")
# b = len(a)
# print("字符串长度为：",b)

# #元组  （）,取值 ，下标
# a = ("哈哈"，"空手牌"，121，True,False,None,1.2)
# print(a)
# print(a[1])
# print(a.index(1.2))

# 元组,下标，从0开始编号
# a = (1,2,3,4,"哈哈哈","哈哈哈","哈哈哈","哈哈哈","嘻嘻嘻",True,False)
# # #print(a[5])
# # print(a.index("哈哈哈"))
# # print(a.count("哈哈哈"))

# #切片
# print(a[0:4])      #左闭右开原则
# print(a[:4])     #从最开始到第四个
# print(a[4:8])
# print(a[9:])     #从第九个到最后

#二维元组的操作
# b = (a,"哈哈哈","嘻嘻嘻")
# print(b[0][3])    #打印a中的某个值

# a = [1,2,3,4,"哈哈哈","嘻嘻嘻",True,False]
# #print(a[4])
# a.append("append")   #往数组中追加数据
# print(a)
# #元组一旦写好以后不能更改，而数组是可以修改的
# a.insert(0,"insert")   #往数组中指定的位置插入数据
# print(a)
# b = a.pop(5)    #剪切
# print(a)
# print(b)


# xx = ["你好","不好"]
# a.extend(xx)         #清空数组       和print(a+xx)效果一样
# print(a)

# # True = 1
# # False = 0

# # 下标不要超出范围 = 越界
# xx = [a,0,1,2,3]   #二维数组

"""
python的语法
所有的方法都是小括号结尾，比如，print(),input(),len()
元组、数组、字典的取值，都是用中括号，比如 a[0]
元组、数组、字典的定义分别是 (),[],{}
"""


"""
字典的特点
1、字典中的值没有顺序。
2、字典的接口必须是 键值对 的结构。   key:value
3、字典的取值，是通过key去取这个value
"""
a = {"name":"张三",
     "age":25
    }

#取值
print(a["name"])
#新增
a["high"] = "180cm"
print(a)
#修改
a["name"] = "李四"
print(a)

b = a.get("name")
print(b)

b = a.pop("name")
print(b)
print(a)

a.update(name="张三")
print(a)

# 数组和字典的删除
#del a["name"]
#print(a)

#0del a[0]

