import cv2
import numpy as np
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
height, width = image.shape[:2]

# Define source points (the four corners of a rectangle)
src_pts = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])

# Define destination points (adjust as needed for perspective transformation)
dst_pts = np.float32([[0, 0], [width - 1, 0], [width*0.8, height - 1], [width*0.2, height - 1]])

# Calculate perspective transformation matrix
transform_matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
perspective_image = cv2.warpPerspective(image, transform_matrix, (width, height))
cv2.imshow('Perspective Transformed Image', perspective_image)

