import cv2
from ultralytics import YOLO

# Load YOLOv8 model (Pre-trained on COCO dataset)
model = YOLO(r'C:\Users\rites\Downloads\ultralytics-main\runs\detect\train17\weights\best.pt')  # Using yolov8n as it's smaller and faster

# Open webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# COCO class IDs for fruits and vegetables
leaf_classes_ids = [0, 1, 2]  # banana, apple, orange, broccoli, carrot

# Run detection loop
while True:
    ret, frame = cap.read()  # Capture frame-by-frame

    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform object detection, restricting to fruit/vegetable classes
    results = model(frame, classes=leaf_classes_ids)  # COCO classes for fruits/vegetables

    # Annotate detected objects on frame
    annotated_frame = results[0].plot()

    # Display the frame with detection
    cv2.imshow('YOLOv8 Real-Time Detection', annotated_frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
