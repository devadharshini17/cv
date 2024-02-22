import cv2
import numpy as np
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
height, width = image.shape[:2]

src_pts = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
dst_pts = np.float32([[0, 0], [width - 1, 0], [width*0.8, height - 1], [width*0.2, height - 1]])

homography_matrix = cv2.findHomography(src_pts, dst_pts)[0]
transformed_image = cv2.warpPerspective(image, homography_matrix, (width, height))

cv2.imshow('Transformed Image', transformed_image)

