"""
字典使用 {} 定义，是 无序的对象集合；
字典使用 键值对 存储数据，其间使用 , 分隔；
键 key 是索引，值 value 是数据；
键值之间使用 : 分隔；
键必须是唯一的，且必须为字符串、数字或元组，值可以为任何数据类型。
"""
GouKong = {
    'name': "GouKong",
    'age': 40,
    'weight': "80kg",
    'height': 188
}
print(GouKong)

# 常用操作
print(GouKong['name'])  # 取值
GouKong['gender'] = 'male'  # 添加
GouKong['age'] = 45  # 修改
del GouKong['height']  # 删除
GouKong.pop('weight')
print(GouKong)

# 字典的统计、合并与清空
print(len(GouKong))  # 统计键值对
GouKong2 = {
    'like': 'fight',
    'wife': 'QiQi'
}
GouKong.update(GouKong2)  # 合并
print(GouKong)
GouKong.clear()  # 清空
print(GouKong)

