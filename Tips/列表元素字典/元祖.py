"""
Tuple 元组与列表类似，最大的区别是元组的 元素不能修改
元组表示多个元素组成的序列，用于存储一串信息，数据之间使用 ， 分隔；
元组使用 ( ) 定义，索引从 0 开始。
"""
yz1 = ("yeXiu",)
yz2 = ("MiDouZi", "ShanYi")

# 常用操作
print(yz2[1])
print(yz2.index("MiDouZi"))  # 读取索引
print(yz2.count("MiDouZi"))  # 统计次数

# 遍历
for i in yz2:
    print(i)

# 元组与列表转换
myList = list(yz2)
print(type(myList), myList)
myTuple = tuple(myList)
print(type(myTuple), myTuple)



