from ultralytics import YOLO
import cv2

model=YOLO("yolov8n.pt")
video_path="sample.mp4"
cap=cv2.VideoCapture(video_path)

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    
    results=model(frame,verbose=False)
    annotated_frame=results[0].plot()
    
    cv2.imshow("Driving Assist AI",annotated_frame)
    
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()