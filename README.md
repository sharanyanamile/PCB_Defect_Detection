PCB Defect Detection System

An AI-based system for automatic detection of defects in Printed Circuit Boards (PCBs) using YOLOv8, FastAPI, and Streamlit.

🚀 Features

Detects 6 PCB defects (missing_hole, mouse_bite, short, open_circuit, spur, spurious_copper)
Multiple image upload support
Annotated output images
Detection details with confidence scores
Download results as images or ZIP

🛠️ Tech Stack
Model: YOLOv8 (trained for 80 epochs)
Backend: FastAPI
Frontend: Streamlit
Libraries: OpenCV, NumPy, Pandas

📊 Performance
mAP@0.5: ~91%
Precision: ~92%
Recall: ~86%


▶️ How to Run
Backend
uvicorn main:app --reload

Frontend
streamlit run pcb_app.py

🏭 Applications
PCB manufacturing quality inspection
Automated visual inspection systems
Electronics industry automation


✅ Conclusion
A complete end-to-end AI solution for PCB defect detection with a professional UI and scalable backend.
