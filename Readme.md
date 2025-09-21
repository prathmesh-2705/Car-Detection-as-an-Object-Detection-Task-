# Car Detection using Object Detection (YOLOv5)
Object Detection is a key area of Computer Vision that allows machines to not only identify what objects are present in an image but also determine their location. 
This is achieved by combining classification (what the object is) with localization (where the object is).

Unlike image classification, which only answers “What is in the image?”, object detection answers “What objects are present, and where are they located?” using bounding boxes around each detected object.

🔍 Object Detection Techniques

Traditional Methods (Before Deep Learning)

Used handcrafted features such as HOG (Histogram of Oriented Gradients), SIFT (Scale Invariant Feature Transform), and Haar Cascades.

Worked for simple tasks like face or pedestrian detection.

Limitations: Not robust to background noise, scale variation, or complex object shapes.

Deep Learning-Based Methods (Modern Approach)

Use Convolutional Neural Networks (CNNs) to automatically learn features.

Examples: Faster R-CNN, SSD (Single Shot Detector), YOLO (You Only Look Once).

Advantages: High accuracy, robust against variations, capable of real-time performance.

YOLO (You Only Look Once)

Divides the image into a grid and predicts bounding boxes + class probabilities in a single pass.

Much faster than older region-proposal-based models.

Suitable for real-time detection tasks like traffic surveillance and autonomous driving.

⚙️ Process of Object Detection

The overall process of detecting a car (or any object) can be divided into the following steps:

Input Acquisition

An image or video is provided as input to the detection system.

Preprocessing

The input frame is resized and normalized to match the model’s requirements.

This reduces computational load and ensures consistent input.

Feature Extraction (CNN)

The deep learning model extracts features from the image, such as edges, shapes, and textures.

These features help differentiate between vehicles and the background.

Bounding Box Prediction

The model predicts bounding boxes around potential objects.

Each bounding box is associated with a confidence score.

Classification

The detected object is classified into categories (e.g., car, truck, bus, motorcycle).

Filtering & Thresholding

Detections with confidence scores below a threshold (e.g., 0.5) are discarded.

Non-Maximum Suppression (NMS) removes overlapping bounding boxes to keep only the best detection.

Output Visualization

Bounding boxes are drawn around detected objects along with labels and confidence scores.

🚘 Car Detection as an Application

In this practical, car detection is implemented using YOLOv5. The goal is to:

Detect different vehicle types such as cars, motorcycles, buses, and trucks.

Draw bounding boxes with confidence scores around each detected vehicle.

Achieve real-time detection when applied to video input.

Car detection plays a vital role in:

Traffic monitoring and management.

Smart cities and automated surveillance systems.

Autonomous driving systems.
