import numpy as np
import matplotlib.pyplot as plt

# # 不同种类不同颜色的线
# x = np.linspace(0, 10, 100)
# plt.plot(x, x + 0, '-g')  # 实线  绿色
# plt.plot(x, x + 1, '--c')  # 虚线 浅蓝色
# plt.plot(x, x + 2, '-.k')  # 点划线 黑色
# plt.plot(x, x + 3, '-r')  # 实线  红色
# plt.plot(x, x + 4, 'o')  # 点   默认是蓝色
# plt.plot(x, x + 5, 'x')  # 叉叉  默认是蓝色
# plt.plot(x, x + 6, 'd')  # 砖石  红色
# plt.show()

# 不同种类不同颜色的线并添加图例
x = np.linspace(0, 10, 100)
plt.plot(x, x + 0, '-g', label='-g')  # 实线  绿色
plt.plot(x, x + 1, '--c', label='--c')  # 虚线 浅蓝色
plt.plot(x, x + 2, '-.k', label='-.k')  # 点划线 黑色
plt.plot(x, x + 3, '-r', label='-r')  # 实线  红色
plt.plot(x, x + 4, 'o', label='o')  # 点   默认是蓝色
plt.plot(x, x + 5, 'x', label='x')  # 叉叉  默认是蓝色
plt.plot(x, x + 6, 'dr', label='dr')  # 砖石  红色
# 添加图例右下角lower right  左上角upper left 边框  透明度  阴影  边框宽度
plt.legend(loc='lower right', fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.show()
