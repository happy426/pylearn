import cv2


img = cv2.imread('data/meinv.jpg')
cv2.imshow('a frame', img)
# 显示一张图片，直至有任意按键被按下则关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()


# 连续显示一组照片，当按下q时，退出显示
# import cv2
#
# i = 1  # the tag of the first image
# while 1:
#     img = cv2.imread('img_' + str(i) + '.png')
#     if img is None:
#         break
#
#     cv2.imshow('frames', img)
#     key = cv2.waitKey(200)  # delay 200ms
#
#     if key == ord('q'):
#         break
#     i = i + 1
# cv2.destroyAllWindows()
