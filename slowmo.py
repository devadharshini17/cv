import cv2
vid=r"C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\pexels_videos_1481903 (1080p).mp4"
cap = cv2.VideoCapture(vid)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video', frame)
    if cv2.waitKey(90) & 0xFF == ord('q'):
        break


