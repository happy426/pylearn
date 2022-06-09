import pandas as pd

a_series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# 索引
a_series.index.name = 'index'
# 值
a = a_series.values
print(a)
print(a_series)
# # 查找元素
# print(a_series.iloc[0])  # 按照绝对位置查找
# print(a_series.loc['a'])  # 按照索引查找

# 统计属性
print(a_series.count())  # 元素个数
print(a_series.dtype)
print(a_series.describe())

# 两个序列相加, 按照index自动匹配，无法匹配的则输出NaN：
b_series = pd.Series([1, 2, 3], index=['百度', '腾讯', '阿里'])
c_series = pd.Series([1, 3, 5], index=['百度', '阿里', '字节'])
d_series = b_series + c_series
print(d_series)



