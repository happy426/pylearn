import time
import requests
import threading

url_list = [
    ('1.jpg',
     'https://c-ssl.duitang.com/uploads/blog/202101/12/20210112105628_56c3a.thumb.1000_0.jpg'),
    ('2.png',
     'https://img.zcool.cn/community/017d0d5ac2d3a1a801212573895b7c.png@1280w_1l_2o_100sh.png'),
    ('3.jpg',
     'https://pic2.zhimg.com/v2-03d0c41725463f2ce3f4214d04c49f16_r.jpg')
]


class MyThread(threading.Thread):
    def run(self):
        name, url = self._args
        res = requests.get(url)
        with open(f'./photo/{name}', 'wb') as f:
            f.write(res.content)
        # 显示时间
        print(time.time())


# 普通下载
# for name, url in url_list:
#     task(name, url)

# 多线程下载
for item in url_list:
    t1 = MyThread(args=(item[0], item[1]))
    t1.start()
