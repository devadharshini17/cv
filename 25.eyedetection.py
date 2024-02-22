import cv2 
img = cv2.imread(r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\eyes.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path=r'C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\eyeee.xml'
eye_cascade = cv2.CascadeClassifier(path) 
eyes= eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) 
for (x, y, w, h) in eyes: 
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
cv2.imshow('Faces Detected', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
