import cv2
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
bigger_image = cv2.resize(image, None, fx=2, fy=2)
smaller_image = cv2.resize(image, None, fx=0.5, fy=0.5)
cv2.imshow('Bigger Image', bigger_image)
cv2.imshow('Smaller Image', smaller_image)

