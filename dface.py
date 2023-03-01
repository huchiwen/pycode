import face_recognition
import os
import cv2

# 加载图像
image = face_recognition.load_image_file("2.jpg")
#如果没有BGR转RGB 显示的图片的颜色不对 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# 获取图像中所有人脸的位置
face_locations = face_recognition.face_locations(image)

# 打印图像中找到的人脸数
print(f"Found {len(face_locations)} face(s) in the image.")

# 循环遍历每张人脸并标记出来
for face_location in face_locations:
    # 获取人脸的坐标
    top, right, bottom, left = face_location

    # 在图像中标记人脸
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

# 显示带有人脸标记的图像
cv2.imshow("Faces found", image)
cv2.waitKey(0)

