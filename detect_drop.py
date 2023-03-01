# 检测人跌倒
import cv2
import numpy as np
import time
from PIL import Image,ImageDraw,ImageFont

# 项目地址
# https://blog.csdn.net/weixin_42990464/article/details/122561746
#
# fontStyle 是根据你系统的字体，教程的系统是Windows，它的字体和mac的不，
# mac 系统用下面的方法就可以了
def cv2ImgAddText(img,text,left,top,textColor=(0,255,0),textSize=20):
    if (isinstance(img,np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontStyle = ImageFont.truetype(
           "Chalkduster.ttf",textSize,encoding="utf-8")
    draw.text((left,top),text,textColor,font = fontStyle)
    return cv2.cvtColor(np.asarray(img),cv2.COLOR_BGR2RGB)

if __name__ == "__main__":
  
  cam = cv2.VideoCapture(r"aaa.mp4")
  cam.set(3,640)
  cam.set(4,480)

  scale = 0
  bg_subtractor = cv2.createBackgroundSubtractorMOG2()

  while True:
      ret,img = cam.read()

      image = img.copy()

      #图片预处理
      blurred = cv2.GaussianBlur(image,(3,3),0)
      gray = cv2.cvtColor(blurred,cv2.COLOR_RGB2GRAY)
      xgrad = cv2.Sobel(gray,cv2.CV_16SC1,1,0)
      ygrad = cv2.Sobel(gray,cv2.CV_16SC1,0,1)

      edage_output = cv2.Canny(xgrad,ygrad,50,150)
      cv2.imshow('edage_output',edage_output)

      fg_mask = bg_subtractor.apply(img)
      #闭运算
      hline = cv2.getStructuringElement(cv2.MORPH_RECT,(1,4),(-1,-1))
      vline = cv2.getStructuringElement(cv2.MORPH_RECT,(4,4),(-1,-1))
      
      result = cv2.morphologyEx(fg_mask,cv2.MORPH_CLOSE,hline)
      result = cv2.morphologyEx(result,cv2.MORPH_CLOSE,vline)

      cv2.imshow('result',result)

      dilateim = cv2.dilate(result,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4)),iterations =1)
      
      #查找轮廓
      countours,hier = cv2.findContours(dilateim,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
      #print(countours,hier)
      for c in countours:
          if cv2.contourArea(c) > 1200:
              (x,y,w,h) = cv2.boundingRect(c)
              if scale ==0:scale = -1;break;
              scale = w/h
              #FONT_HERSHEY_SIMPLEX 教程的和我这里的不一样，以我的代码为标准.
              cv2.putText(image,"scale:{:.3f}".format(scale),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
              #cv2.drawContours(image,[c],-1,(255,0,0),1)
              cv2.rectangle(image,(x,y),(x + w,y + h),(0,255,0),1)
              #image = cv2.fillPoly(image,[c],(255,255,255))


      #if scale > 0 and scale <1:
      #    img = cv2ImgAddText(img,"walking",10,20,(250,0,0),30)
      if scale > 0.9 and scale < 2:
          #img = cv2ImgAddText(img,"falling",10,20,(250,0,0),30)
          image = cv2ImgAddText(img,"someone falling",10,20,(250,0,0),30)
      #if scale > 2:
      #    img = cv2ImgAddText(img,"Falled",10,20,(250,0,0),30)

      #cv2.imshow('Foregound Mask',fg_mask)
      cv2.imshow('test',image)
      #cv2.imshow('image',img)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  cam.release()
  cv2.destroyAllWindows()

