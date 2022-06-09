"""
cv2.imread(filepath,flags)     #读入一张图像
filepath：要读入图片的完整路径
flags：读入图片的标志
cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
cv2.IMREAD_GRAYSCALE：读入灰度图片
cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道

cv2.imshow(wname,img)     #显示图像
第一个参数是显示图像的窗口的名字
第二个参数是要显示的图像（imread读入的图像），窗口大小自动调整为图片大小

cv2.cvtColor()      #图像颜色空间转换

img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)   #灰度化：彩色图像转为灰度图像
img3 = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)   #彩色化：灰度图像转为彩色图像
# cv2.COLOR_X2Y，其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS
cv2.resize(image, image2,dsize)     #图像缩放：(输入原始图像，输出新图像，图像的大小)
cv2.flip(img,flipcode)                       #图像翻转，flipcode控制翻转效果。

flipcode = 0：沿x轴翻转；flipcode > 0：沿y轴翻转；flipcode < 0：x,y轴同时翻转
cv2.warpAffine(img, M, (400, 600))       #图像仿射变换 ：平移；裁剪、剪切、旋转、仿射变换，
M、M_crop、M_shear、M_rotate

cv2.putText(img,'text',(50,150)   #图像添加文字：(照片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细)

cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)    #画出矩行：img原图、(x，y)是矩阵的左上点坐标、
(x+w，y+h)是矩阵的右下点坐标、(0,255,0)是画线对应的rgb颜色、2是所画的线的宽度。

cv2.boundingRect(img)
#返回图像的四值属性：img是一个二值图，即是它的参数； 返回四个值，分别是x，y，w，h； x，y是矩阵左上点的坐标，w，h是矩阵的宽和高。
"""
import cv2

# 读取图片
img0 = cv2.imread('data/meinv.jpg', 0)
img = cv2.imread('data/meinv.jpg')
print(img.shape)
print(img)
print(img[0])
print(img[0][0])

print(img0.shape)
print(img0)
print(img0[0])
print(img0[0][0])
# # 写入图片
# cv2.imwrite('data/meinv2.jpg', img[0:1400, 240:1640])

