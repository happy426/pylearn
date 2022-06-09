import numpy as np
import pandas as pd


data = pd.DataFrame(np.arange(12).reshape(3, 4))
print(data)
# print(data[3][2])
# # 按照列降序排序
# print(data.sort_values(by=0, ascending=False))
# # 按照行降序排序
# print(data.sort_values(by=0, ascending=False, axis=1))


