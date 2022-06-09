import cv2 as cv
import numpy as np
import random

# 将图片数据读取进来
img = cv.imread("../data/888157224.jpeg", cv.COLOR_BGR2GRAY)
cv.imshow("img", img)

# # 1. 将图片转成灰度图片
# grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. canny算法
dstImg = cv.Canny(img, 50, 180)

# 显示效果图
cv.imshow('dstimg', dstImg)
cv.waitKey(0)
cv.destroyAllWindows()

