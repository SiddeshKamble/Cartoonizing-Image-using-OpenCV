
# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt

#Defined a function to take images
def Image(img):
  cv2.imshow("img",img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
#Definying the path of the image
path = "C:/Users/Siddesh/Desktop/kobe.jpg"
#showing the image
img = cv2.imread(path)
Image(img) 

col_img =  cv2.bilateralFilter(img,5,255,255)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)

edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)

Image(edges)
cartoon = cv2.bitwise_and(col_img,col_img,mask = edges)
Image(cartoon)
