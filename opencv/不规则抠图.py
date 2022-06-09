import cv2

img = cv2.imread('data/meinv.jpg')
print(img[5][1][1])
# zuo_xia_y = 1000
# zuo_shang_y = 150
# zuo_xia_x = 200
# you_xia_x = 1300
# crop_img = img[int(zuo_shang_y):int(zuo_xia_y), int(zuo_xia_x):int(you_xia_x)]
# cv2.imwrite('data/bgz.jpg', crop_img)
