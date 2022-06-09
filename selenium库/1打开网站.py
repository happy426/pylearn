"""
下载：
pip install selenium -i https://pypi.douban.com/simple/
chromedriver放在bin目录下就不用使用Service了。
"""
from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.service import Service
#
# s = Service('/Users/smai/Desktop/tool/chromedriver')
# 创建浏览器对象
web = Chrome()

# 获取网站
web.get('https://www.baidu.com')

# 关闭网站
# web.close()


