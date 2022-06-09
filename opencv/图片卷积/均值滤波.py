"""
将卷积核内的所有灰度值加起来,然后计算出平均值,用这个平均值填充卷积核正中间的值,这样做可以降低图像的噪声,同时也会导致图像变得模糊
"""
import cv2

img = cv2.imread('../data/888157224.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)
print(img[0])
ksize = (10, 10)  # 算子
dst = cv2.blur(img, ksize)
cv2.imshow('dst', dst)
print(dst[0])
cv2.waitKey(0)
cv2.destroyAllWindows()


