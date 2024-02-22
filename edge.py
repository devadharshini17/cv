import cv2
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
cv2.imshow('Original Image', image)
cv2.imshow('Sobel X Edge Detection', sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
