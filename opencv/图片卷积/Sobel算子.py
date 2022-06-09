import cv2

img = cv2.imread('../data/street.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

# sobel算子 参数1：图像 参数2：图像的深度 -1表示和原图相同 参数3：x方向求导的阶数 参数4：y方向求导的阶数
x_sobel = cv2.Sobel(img, cv2.CV_32F, 1, 0)
# 将图像转换成8位int
x_sobel = cv2.convertScaleAbs(x_sobel)

cv2.imshow('x_sobel', x_sobel)

# sobel算子
y_sobel = cv2.Sobel(img, cv2.CV_16S, 0, 1)
# 将图像转换成8位int
y_sobel = cv2.convertScaleAbs(y_sobel)
cv2.imshow('y_sobel', y_sobel)

# 将x,y方向的内容叠加起来
x_y_sobel = cv2.addWeighted(x_sobel, 0.5, y_sobel, 0.5, 0)
cv2.imshow('x_y_sobel', x_y_sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
