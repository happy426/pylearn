"""
numpy二维数组则是一个矩阵，较一维数组多了一个“轴”，有行也有列。
类似地，创建numpy二维数组，传入一个嵌套列表即可，每个子列表的元素数目相同，有多少个子列表，二维数组就有多少行。
"""
import numpy as np

# 创建随机数2维数组
a2d = np.array(np.random.randint(1, 10, 12).reshape(3, 4))
# print(a2d)
# 创建序列2维数组
b2d = np.array(np.arange(12).reshape(3, 4))
print(b2d)
print(b2d[2, 2])
print(b2d[2, :])  # 第3行
print(b2d[:, 2])  # 第3列
print(b2d.mean())
print(b2d.mean(axis=0))  # 每一列的平均值
print(b2d.mean(axis=1))  # 每一行的平均值

