import cv2
path = r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\cat.jpg'
image = cv2.imread(path)
affine_image = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1]/2, image.shape[0]/2), 30, 1), (image.shape[1], image.shape[0]))
cv2.imshow('Affine Transformed Image', affine_image)

