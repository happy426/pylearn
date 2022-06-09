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

print(df_score.loc[[0, 1], ['name', 'math']])  # 第一行和第二行的名字与数学成绩
print(df_score.loc[[0, 2], :])
