"""
DataFrame可以看成是由若干Series组合而成，这些Series共享同一index行索引，列索引则包含所有Series的列名称，行索引和列索引均有name属性。
标准的DataFrame结构包含：
①数据内容部分df.values，它是一个numpy的ndarray类型
②行索引df.index，列索引df. columns
③行索引的名字df.index.name，和列索引的名字df.columns.name
"""
import pandas as pd


# 创建DataFrame可以将一个（有序）字典传入函数，字典的键key将自动变成数据框的列索引columns，
# 如果不显式指定行索引index，则系统自动生成整数型行索引0 1 2 3……
score_dict = {
    "name": ['zs', 'wr', 'mz'],
    "math": [100, 60, 88],
    "English": [100, 66, 77],
    'chinese': [99, 59, 89],
    "date": ['2020', '2020', '2020']
}
df_score = pd.DataFrame(score_dict)
print(df_score)

print(df_score.columns)
print(df_score.index)

# # 统计信息
# print(df_score.count())  # 自动按列统计
# print(df_score.describe())

print("英语成绩为：\n", df_score.iloc[:, 2])  # 第三列
print("zs的成绩为：\n", df_score.iloc[0, :])
print("zs和mz的成绩为：\n", df_score.iloc[[0, 2], :])  # 切片

