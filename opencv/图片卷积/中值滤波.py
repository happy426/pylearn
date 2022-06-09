"""
对邻近的像素点进行灰度排序,然后取中间值,它能有效去除图像中的椒盐噪声

操作原理: 卷积域内的像素值从小到大排序 取中间值作为卷积输出
"""
import cv2


img = cv2.imread('../data/888157224.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)

mid = cv2.medianBlur(img, 3)
cv2.imshow('mid', mid)

cv2.waitKey(0)
cv2.destroyAllWindows()





