import numpy as np
import matplotlib.pyplot as plt
import math


x = np.linspace(-10, 10, 100)
sin = []
cos = []
tan = np.tan(x)
for i in x:
    sin.append(math.sin(i))
    cos.append(math.cos(i))

# 创建画布
figure = plt.figure('figure', figsize=(10, 6), dpi=100)

# 创建子图
sin_p = figure.add_subplot(2, 2, 1)
cos_p = figure.add_subplot(2, 2, 2)
tan_p = figure.add_subplot(2, 2, 3)
num = figure.add_subplot(2, 2, 4)

# 在不同的轴域画图形
sin_p.plot(x, sin)
cos_p.plot(x, cos)
tan_p.plot(x, tan)
num.plot(x)

# 图片名称
plt.suptitle('photo')

# 子图名字
sin_p.set_title('sin_photo')

plt.show()









