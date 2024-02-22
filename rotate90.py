import cv2
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
ri=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated",ri)
cv2.imshow("org",image)
