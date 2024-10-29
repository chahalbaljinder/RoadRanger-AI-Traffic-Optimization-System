import cv2
import torch

# Load YOLOv5 pre-trained model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_vehicles(frame):
    results = model(frame)
    # Returns the count of detected vehicles
    return results.xyxy[0].shape[0]
