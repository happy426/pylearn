"""
选择到元素之后，我们的代码会返回元素对应的 WebElement对象，通过这个对象，我们就可以 操控 元素了。
操控元素通常包括
点击元素
在元素中输入字符串，通常是对输入框这样的元素
获取元素包含的信息，比如文本内容，元素的属性
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

diver = Chrome()
diver.get('https://www.csdn.net/')
web = diver.find_element(By.CSS_SELECTOR, '#toolbar-search-input')
# 输入框
web.clear()  # 清除输入框已有的字符串
web.send_keys('selenium')  # 输入新字符串
time.sleep(1)
bottom = diver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/button/span')
bottom.click()
