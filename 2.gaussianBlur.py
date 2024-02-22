import cv2 
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png'
img =cv2.imread(path) 
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) 
cv2.imshow("Img Blur",imgBlur)
cv2.imshow("image",img)
