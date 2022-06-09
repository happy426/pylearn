"""
List 列表是 Python 中使用最频繁的数据类型，在其他语言中通常为数组；
列表用于存储一串信息，使用 [ ] 定义，数据之间使用 ， 分隔；
列表的索引，也可以称之为下标，是从 0 开始的
"""
name = ['huang', 'peng', 'sheng', 'xu']

print(name[0])  # 查找元素
name[0] = 'er_gou'  # 修改值
print(name)

# 增加元素
name.append('yeXu')  # 向列表的末尾追加数据
name.insert(0, 'suMuCheng')  # 在列表的指定索引位置插入数据
name2 = ['miTouZi', 'TanZhiLang']
name.extend(name2)  # 将一个列表拼接到列表的末尾
print(name)

# 删除元素
name.remove('er_gou')  # 删除列表中指定数据（多次出现则删除第一个，如果没有则报错）
name.pop(-3)  # 在不使用参数 index 时，默认删除并返回列表末尾的数据；使用参数 index 可以指定希望删除数据的索引
name.pop()
name2.clear()  # 清空列表
print(f"name:{name}, name2:{name2}")

# 统计
print(f"name的元素个数：{len(name)}")
print(f"name中'peng'的个数：{name.count('peng')}")

# 排序
nums = [5, 2, 3, 9, 1, 2, 7]
nums.sort()
print(f"升序排序：{nums}")
nums.sort(reverse=True)
print(f"降序排序：{nums}")
nums.reverse()
print(f"反转：{nums}")

# 元素遍历
for i in nums:
    print(i)

