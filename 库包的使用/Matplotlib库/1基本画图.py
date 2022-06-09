"""
下载库包  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
"""
import matplotlib.pyplot as plt
import math

x = list(range(10))
y = []
for i in x:
    y.append(math.e**i)
print(x, y)

plt.plot(x, y, color='r', linewidth=5)  # 画图，设置线的信息
plt.title('e', fontsize=24)  # 图片命名
plt.xlabel('x')  # x轴命名
plt.ylabel('y')  # y轴命名
plt.show()  # 图片展示


