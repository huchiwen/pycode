import cv2 
import numpy as np
import pickle
import os
import face_recognition

cap = cv2.VideoCapture(0)

#  cap.set(3,640) 3 代表 宽度
#  cap.set(4,480) 4 代表 高度

#  CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
#  CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.

#  see https://blog.csdn.net/leon_zeng0/article/details/102791988
#
#
cap.set(3,640) # width
cap.set(4,480) # height

img_background = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
model_path = os.listdir(folderModePath)

#print(type(model_path))
#exit()

imgModeList = []

for index in model_path:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, index)))

#print(imgModeList)
print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close() 

encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded")


while True:

  success,img = cap.read()

  imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
  imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

  #检测出所有人脸的位置,
  #它会返回一个列表，其中包含图像中每个人脸的位置。每个位置表示为一个四元组 (top, right, bottom, left)，其中 (top, left) 是人脸矩形框的左上角坐标，(bottom, right) 是人脸矩形框的右下角坐标。

  faceCurFrame = face_recognition.face_locations(imgS)
  #人脸编码
  encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

  img_background[162:162 + 480, 55:55 + 640] = cv2.resize(img, (640, 480))

  if faceCurFrame:
    for eface,faceL in zip(encodeCurFrame,faceCurFrame):
        #待比较的人脸是否与已知人脸匹配
        matches = face_recognition.compare_faces(encodeListKnown,eface)
        #利用已知人脸的特征向量列表，计算待比较人脸与每个特征向量之间的欧氏距离
        faceDis = face_recognition.face_distance(encodeListKnown,eface)

        #print(matches) #返回[False,False,False]
        print(faceDis)
        #np.argmin() 返回数组中的最小值的下标
        match_index = np.argmin(faceDis)
        #print('相似度为%f,最小值为%s'%(1-faceDis[match_index],' ' + str(faceDis[match_index])))

  #cv2.imshow("webcame",img)
  cv2.imshow("Face Attendance",img_background)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break;
cap.release()
cv2.destroyAllWindows()
