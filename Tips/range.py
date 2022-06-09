"""
range(start, stop[, step])
参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

相当于：start + step，到stop为止
"""
for x in range(0, 5, 2):
    print(x, end=',')  # 0, 2, 4

print("\n" + "**"*20)

for i in range(5, 0, -1):
    print(i, end=',')  # 5, 4, 3, 2, 1
