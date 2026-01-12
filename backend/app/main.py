from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
from PIL import Image
import io
import numpy as np
import json

app = FastAPI()

model = YOLO("A:/dataset/runs/pcb_yolov8n_ft/weights/best.pt")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    results = model.predict(
        source=np.array(image),
        conf=0.5,
        iou=0.45,
        imgsz=640,
        verbose=False
    )

    result = results[0]

    # ---- Detection details ----
    detections = []
    if result.boxes is not None:
        for box in result.boxes:
            detections.append({
                "class": result.names[int(box.cls)],
                "confidence": float(box.conf),
                "bbox": box.xyxy.tolist()
            })

    # ---- Annotated image ----
    annotated = result.plot()[:, :, ::-1]
    annotated_img = Image.fromarray(annotated)

    buf = io.BytesIO()
    annotated_img.save(buf, format="PNG")
    buf.seek(0)

    headers = {
        "X-Detections": json.dumps(detections)
    }

    return StreamingResponse(buf, media_type="image/png", headers=headers)
