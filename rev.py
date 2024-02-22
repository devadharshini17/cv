import cv2
vid=r"C:\Users\bharath kumar\AppData\Local\Programs\Python\Python312\pexels_videos_1481903 (1080p).mp4"
cap = cv2.VideoCapture(vid)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

for frame_number in range(total_frames - 1, -1, -1):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Reversed Video', frame)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
