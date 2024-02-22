#Convert an Image to Grayscale 
import cv2 
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png'
img =cv2.imread(path) 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow("GrayScale",imgGray) 
cv2.waitKey(0) 
 
