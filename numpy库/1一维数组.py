"""
创建numpy一维数组，需要传入一个列表参数，其元素查找方式类似于列表，但又和列表有着截然不同的区别：
区别一：array数组元素的数据类型必须一致，列表可以包含不同的数据类型
区别二：array可以进行向量计算
区别三：array具有统计功能
区别四：array数组乘以标量n表示每个元素值放大n倍，列表乘以标量n表示重复n次
"""
import numpy as np

# 数组
a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])
# 列表
a_list = [1, 2, 'three', '四', 5]

print(a_array[2], " ", a_list[2])
print(a_array*2, " ", a_list*2)

print(a_array+b_array)
print(a_array.mean(), a_array.sum(), a_array.min())

