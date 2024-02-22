import cv2
path = r"C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg"
img =cv2.imread(path) 
erode=cv2.erode(img,None,iterations=1)
cv2.imshow("err",erode)
cv2.imshow("Image",img)


