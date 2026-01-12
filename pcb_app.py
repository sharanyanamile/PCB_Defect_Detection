import streamlit as st
import requests
from PIL import Image
import io
import json
import zipfile
import pandas as pd

st.set_page_config("PCB Defect Detection", "🧠", layout="wide")

st.title("🧾 PCB DEFECT DETECTION")
st.caption("Frontend connected to FastAPI backend using YOLOv8")

BACKEND_URL = "http://127.0.0.1:8000/detect"

uploaded_files = st.file_uploader(
    "📤 Upload PCB Images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

all_images = []
all_rows = []

if uploaded_files:
    for idx, file in enumerate(uploaded_files):
        st.subheader(f"🖼 Image {idx+1}: {file.name}")

        col1, col2 = st.columns(2)

        image = Image.open(file)
        col1.image(image, caption="Original Image", use_container_width=True)

        with st.spinner("Running detection..."):
            response = requests.post(
                BACKEND_URL,
                files={"file": (file.name, file.getvalue(), file.type)}
            )

        if response.status_code == 200:
            annotated_img = Image.open(io.BytesIO(response.content))
            col2.image(annotated_img, caption="Detected Defects", use_container_width=True)

            # Save for ZIP
            all_images.append((f"annotated_{file.name}", response.content))

            # Download single image
            st.download_button(
                "⬇️ Download Annotated Image",
                data=response.content,
                file_name=f"annotated_{file.name}",
                mime="image/png",
                key=f"dl_{idx}"
            )

            # ---- Detection details ----
            detections = json.loads(response.headers.get("X-Detections", "[]"))

            if detections:
                for det in detections:
                    all_rows.append({
                        "Image": file.name,
                        "Class": det["class"],
                        "Confidence": round(det["confidence"], 3),
                        "BBox": det["bbox"]
                    })

                st.dataframe(pd.DataFrame(detections), use_container_width=True)
            else:
                st.info("No defects detected")

        else:
            st.error("Backend error")

    # ---- ZIP download ----
    if all_images:
        zip_buf = io.BytesIO()
        with zipfile.ZipFile(zip_buf, "w") as zipf:
            for name, data in all_images:
                zipf.writestr(name, data)

        zip_buf.seek(0)
        st.download_button(
            "⬇️ Download ALL Annotated Images (ZIP)",
            data=zip_buf,
            file_name="pcb_annotated_images.zip",
            mime="application/zip"
        )

    # ---- Combined details ----
    if all_rows:
        st.subheader("📊 All Detection Details")
        st.dataframe(pd.DataFrame(all_rows), use_container_width=True)
