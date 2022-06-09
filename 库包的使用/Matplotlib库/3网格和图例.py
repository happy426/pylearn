import numpy as np
import matplotlib.pyplot as plt


x = np.arange(10)
y = np.sin(x)
plt.plot(x, linestyle='--', label='x')
plt.plot(x, y, linestyle=':', label='sin(x)')

plt.grid(linestyle='--', alpha=0.5)  # 添加网格，设置格式和透明度

plt.legend(loc='best')  # 显示图例， plt.plot中一定要有label才行。

plt.savefig('result/result.jpg')  # 保存图片

plt.show()
