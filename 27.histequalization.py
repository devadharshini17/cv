import cv2 
import numpy as np 
img = cv2.imread(r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png', 0) 
equ = cv2.equalizeHist(img) 
res = np.hstack((img, equ)) 
cv2.imshow("image", res) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
