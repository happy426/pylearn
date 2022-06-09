"""
t.start()  线程开始。
t.join()  等待当前线程的任务执行完毕后再向下执行。主线程等待。
t.setDaemon(布尔值)  守护线程(必须放在start之前)
True 守护线程，主线程关闭，子线程也关闭
False 非守护线程，主线程等待子线程结束才结束。默认
t.setName()  给线程设计名字。
name = threading.current_thread().getName()  获取名字。
"""

import threading


loop = 100000
number = 0


def _add(count):
    global number
    name = threading.current_thread().getName()
    print(name)
    for i in range(count):
        number += 1


def _sub(count):
    global number
    for i in range(count):
        number -= 1


t = threading.Thread(target=_add, args=(loop, ))
t.setDaemon(True)  # 守护线程
t.setName('name')
t.start()

# t.join()  # 主线程等待中。


print(number)
