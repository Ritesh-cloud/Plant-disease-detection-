# Plant-disease-detection-
A custom dataset of annotated plant leaf images was prepared.

The dataset is split into two parts:

Training set

Validation set

Annotations were created in YOLO format.

🧠 Model
YOLOv8n (nano version) was chosen for its speed and efficiency on edge devices.

Training was done using Ultralytics YOLOv8 framework.

🏗️ Training Setup
Framework: Ultralytics YOLOv8

Model: yolov8n

Training command:

bash
yolo task=detect mode=train model=yolov8n.pt data=your_dataset.yaml epochs=100 imgsz=640

Validation and testing used the same dataset format, split accordingly.
