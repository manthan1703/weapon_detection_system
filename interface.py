import streamlit as st
import os
import tempfile
from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")  # firearm-trained model

st.title("🔫 Firearm Detection System")

# Upload video
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
if uploaded_file:
    # Save uploaded file to temp location
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())

    # Run detection directly on video
    results = model.predict(
        source=tfile.name,
        save=True,
        project="runs/detect/",
        name="detect"
    )

    # ✅ Get YOLO's actual save directory
    save_dir = model.predictor.save_dir  

    # ✅ The output video will have the same name as input
    detected_video_path = os.path.join(save_dir, os.path.basename(tfile.name))

    if os.path.exists(detected_video_path):
        st.video(detected_video_path)
    else:
        st.warning("Processed video  found. Check YOLO output folder.")

    # Firearm presence check
    firearm_detected = any(len(r.boxes) > 0 for r in results)
    if firearm_detected:
        st.error("⚠️ Firearm Detected!")
    else:
        st.success("✅ No Firearm Detected")
