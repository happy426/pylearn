"""
高斯函数呈现出的特征就是中间高，两边低的钟形

高斯模糊通常被用来减少图像噪声以及降低细节层次。
"""
import cv2


def updateSigma(val):
    """
    高斯模糊
    :param val: 卷积大小
    :return:
    """
    # 参数1：图像 参数2：卷积核大小 参数3：标准差越大，去除高斯噪声能力越强，图像越模糊
    gaussian_blur = cv2.GaussianBlur(img, (5, 5), val)
    cv2.imshow('gaussian', gaussian_blur)


img = cv2.imread('../data/888157224.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

# 创建一个窗口
cv2.namedWindow("gaussian", cv2.WINDOW_AUTOSIZE)

# 创建一个窗口进度条: 参数1:名称 参数2:窗口名称  参数3: 起始值  参数4: 最大值, 参数5:回调函数
cv2.createTrackbar('sigma', 'gaussian', 0, 255, updateSigma)

updateSigma(0)

cv2.waitKey(0)
cv2.destroyAllWindows()

