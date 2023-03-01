import cv2

image = cv2.imread('lena.jpg')
img1 = cv2.resize(image, (0, 0),None,0.25,0.25)

cv2.imshow("img",img1)
cv2.imshow("origin img",image)
cv2.waitKey(0)

