import cv2
import numpy as np
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png'
img =cv2.imread(path) 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.cornerHarris(gray, 2, 3, 0.05)
corners = cv2.dilate(corners, None)
img[corners > 0.01 * corners.max()]=[0, 0, 255]
cv2.imshow('Image with Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
