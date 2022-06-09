from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

diver = Chrome()
diver.get('https://www.baidu.com')

"""
使用 find_elements 选择的是符合条件的 所有 元素， 如果没有符合条件的元素， 返回空列表
使用 find_element 选择的是符合条件的 第一个 元素， 如果没有符合条件的元素， 抛出 NoSuchElementException 异常

"""
# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = diver.find_elements(By.CLASS_NAME, "title-content-title")
print(elements)
# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for i in elements:
    print(i.text)


"""
# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')
# 根据 class name 选择元素，返回的是 一个列表
# 里面 都是class 属性值为 animal的元素对应的 WebElement对象
elements = wd.find_elements(By.CLASS_NAME, 'animal')
# 根据 tag name 选择元素，返回的是 一个列表
# 里面 都是 tag 名为 div 的元素对应的 WebElement对象
elements = wd.find_elements(By.TAG_NAME, 'div')
"""

"""
可以直接去网站复制路径。
css定位
elements = diver.find_elements(By.CSS_SELECTOR, '')
xpath定位
elements = diver.find_elements(By.XPATH, '')
"""
