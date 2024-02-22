import cv2 
import numpy as np 

path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png'
img =cv2.imread(path) 
 
imgCanny = cv2.Canny(img,200,100) 
cv2.imshow("Img Canny",imgCanny) 
cv2.waitKey(0) 
