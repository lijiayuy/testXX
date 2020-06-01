print("hello word")
print(2333)
print(2.333)
print(None)
print(True,False)
print(())
print({})
print([])

a = "哈哈哈"   #把哈哈哈这个值赋值给变量a
print(a)   #变量不用加引号

name ="张三"
print("你好,{}".format(name))
#这就是单行注释
"""
这是多行注释
数据十一号
"""
print("1,"+"1")
print(1+1)
print((((2+1)*10)/3)-7)
print(2>1)
name = input("请输入你的姓名：")
print("这是input获取的值："，name)

#通过input获取两个数字，并计算他们的和
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数字："))
c = (a+b)
print("两数字之和："，c)

#请实现一个数数字的功能
a = input("请输入内容：")
b = len(a)
print("字符串长度为：",b)

#元组  （）,取值 ，下标
a = ("哈哈"，"空手牌"，121，True,False,None,1.2)
print(a)
print(a[1])
print(a.index(1.2))








