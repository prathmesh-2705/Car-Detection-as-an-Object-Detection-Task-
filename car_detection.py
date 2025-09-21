!pip install ultralytics opencv-python-headless 
import cv2 
import torch 
# Load the YOLOv5 pre-trained model 
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # YOLOv5 small model 
# Provide the absolute path to your video 
video_path = r"C:\HTML\.vscode\vid2.mp4" 
# Access the video using the path 
cap = cv2.VideoCapture(video_path) 
# Vehicle class IDs in the COCO dataset 
VEHICLE_CLASS_IDS = [2, 3, 5, 7]  # Car, Motorcycle, Bus, Truck 
# Set desired frame width and height 
frame_width = 640  # Adjust as needed 
frame_height = 360  # Adjust as needed 
while cap.isOpened(): 
ret, frame = cap.read() 
if not ret: 
break 
# Resize frame to reduce processing load 
    frame = cv2.resize(frame, (frame_width, frame_height)) 
 
    # Perform detection 
    results = model(frame) 
    detections = results.xyxy[0]  # Extract detection results 
 
    for detection in detections: 
        x1, y1, x2, y2, confidence, class_id = detection 
         
        # Filter detections for vehicle classes 
        if int(class_id) in VEHICLE_CLASS_IDS and confidence > 0.5 
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2) 
            label = f'Vehicle: {confidence:.2f}' 
            cv2.putText(frame, label, (int(x1), int(y1) - 10), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) 
    cv2.imshow('Vehicle Detection System', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
cap.release() 
cv2.destroyAllWindows() 
 
 
 
 
 
 
