from cvzone.FaceDetectionModule import FaceDetector
import cv2
 
cap = cv2.VideoCapture(0)
#ret=cap.set(3,2560)
#ret=cap.set(3,720)
 
detector = FaceDetector()
 
while True:
    ret, img = cap.read()
    #cv2.imwrite("./temp/3/1.jpg",img)
    img, bboxs = detector.findFaces(img)
    
    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
 
    cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

