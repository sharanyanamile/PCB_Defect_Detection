PCB Defect Detection System
YOLOv8 | FastAPI | Streamlit

An end-to-end deep learning–based system for automatic detection of defects in Printed Circuit Boards (PCBs) using computer vision. The project integrates a YOLOv8 object detection model, a FastAPI backend, and a Streamlit frontend to deliver an interactive and scalable solution.

📌 Project Overview

Manual PCB inspection is time-consuming, error-prone, and inefficient for large-scale manufacturing.
This project automates the inspection process by detecting common PCB defects with high accuracy.

🎯 Key Objectives

Automate PCB defect detection
Reduce manual inspection effort
Improve detection accuracy and consistency
Provide an easy-to-use web interface

🧠 Defects Detected

The model detects the following 6 PCB defect classes:
missing_hole
mouse_bite
short
open_circuit
spur
spurious_copper

🏗️ System Architecture
User
  ↓
Streamlit Frontend
  ↓ (HTTP Request)
FastAPI Backend
  ↓
YOLOv8 Model (best.pt)
  ↓
Detection Results (Image + JSON)

⚙️ Technologies Used
🔹 Deep Learning

YOLOv8 (Ultralytics)

🔹 Backend

FastAPI
Uvicorn
Python

🔹 Frontend

Streamlit

Custom CSS

🔹 Libraries

OpenCV

NumPy

Pandas

Pillow

📂 Project Structure
dataset/
│
├── backend/
│   └── app/
│       ├── main.py        # FastAPI backend
│       └── requirements.txt
│
├── pcb_app.py             # Streamlit frontend
│
├── runs/
│   └── pcb_yolov8n_ft/
│       └── weights/
│           └── best.pt    # Trained YOLOv8 model
│
├── train/
├── val/
├── data.yaml
└── README.md

🧪 Model Training Details

Model: YOLOv8n

Epochs: 80

Image Size: 640 × 640

Training Type: Transfer learning + fine-tuning

Hardware: CPU

📊 Performance Metrics
mAP@0.5: ~91%
Precision: ~92%
Recall: ~86%

Training curves show steady convergence with minimal overfitting.

🚀 Backend (FastAPI)
Available Endpoints
🔹 Health Check
GET /

🔹 Detect PCB Defects
POST /detect/


Input:

PCB image (jpg / jpeg / png)

Output:

Annotated image

JSON with:

Defect class

Confidence score

Bounding box coordinates

🎨 Frontend (Streamlit)
Features

Upload single or multiple PCB images

View:

Original image

Annotated output image

Detection details table

Download:

Individual annotated images

ZIP of all annotated images

Clean, professional dashboard UI

▶️ How to Run the Project
1️⃣ Start Backend
cd dataset/backend/app
uvicorn main:app --reload


Open API docs:

http://localhost:8000/docs

2️⃣ Start Frontend
streamlit run pcb_app.py

🏭 Applications

PCB manufacturing quality inspection

Automated Visual Inspection (AVI)

Electronics assembly line monitoring

Industry 4.0 smart factories

Academic and research projects

🌱 Future Enhancements

GPU-based deployment for real-time speed

SAM-based segmentation for finer defect analysis

Cloud deployment (AWS / Azure)

Defect severity classification

Database integration for defect history

✅ Conclusion

This project demonstrates a complete AI-based industrial inspection system, integrating:
Deep learning (YOLOv8)
Scalable backend (FastAPI)
User-friendly frontend (Streamlit)
It is industry-ready, extensible, and suitable for real-world deployment.
