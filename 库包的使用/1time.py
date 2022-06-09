import time
from datetime import datetime

before = time.time()  # time.time() 会返回 从 1970年1月1日0点（所谓的epoch时间点） 到 当前时间的 经过的秒数
# print(before)
print(datetime.now())  # 得到 当前时间 对应的字符串
print(datetime.now().strftime('%Y-%m-%d ** %H:%M:%S'))  # 指定输出的时间格式
print(time.strftime('%Y-%m-%d ** %H:%M:%S', time.localtime()))  # time库来格式化显示字符串
# 字符串时间转化为整数时间
print(int(time.mktime(time.strptime('2015-08-01 23:59:59', '%Y-%m-%d %H:%M:%S'))))  # 1438444799
