import cv2
path = r"C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg"
img =cv2.imread(path) 
dilatedimg=cv2.dilate(img,None,iterations=1)
cv2.imshow("dilated",dilatedimg)
cv2.imshow("Image",img)


