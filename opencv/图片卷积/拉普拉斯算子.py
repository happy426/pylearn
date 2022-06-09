"""
通过拉普拉斯变换后增强了图像中灰度突变处的对比度，使图像中小的细节部分得到增强,使图像的细节比原始图像更加清晰。
"""
import cv2

img = cv2.imread('../data/street.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

dst = cv2.Laplacian(img, cv2.CV_32F)
# 取绝对值，将数据转到uint8类型
dst = cv2.convertScaleAbs(dst)

cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()





