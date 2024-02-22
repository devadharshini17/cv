import cv2
import numpy as np
kernel = np.ones((5, 5), np.uint8)
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\tree.png'
original_image = cv2.imread(path, cv2.IMREAD_COLOR)
larger_resized_image = cv2.resize(original_image, (800, 800))
smaller_resized_image = cv2.resize(original_image, (400, 400))
cv2.imshow("Larger Resized Image", larger_resized_image)
cv2.imshow("Smaller Resized Image", smaller_resized_image)
cv2.waitKey(0)
