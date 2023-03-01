import cv2

# 读取图像
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

# 进行Canny边缘检测
edges = cv2.Canny(img, 100, 200)

# 显示原始图像和边缘检测结果
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)

# 等待按下任意按键退出
cv2.waitKey(0)

# 释放窗口资源
cv2.destroyAllWindows()

