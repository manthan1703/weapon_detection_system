cat << 'EOF' > README.md
# 🔫 Weapon Detection System (Firearms & Improvised Weapons)

---

## 🌟 Project Overview
This project implements an **AI-powered weapon detection system** using **YOLOv8**.  
It can automatically detect:  

- **Firearms** (pistols, rifles, guns)  
- **Improvised Weapons** (metal rods, broken glass, sharp objects)  
- **No Weapon** (safety class for better accuracy)  

The system processes **videos or images** to identify and highlight weapons, and includes a **Streamlit web interface** for easy interaction.

---

## 🎯 Security Application Objectives
- **Threat Detection** – Identify firearms and improvised weapons in media.  
- **Enhanced Security** – Provide real-time insights for security personnel.  
- **Scalable Deployment** – Integration with CCTV, drones, and edge devices.  
- **Early Alerts** – Firearm/weapon alert system for quick action.  

---

## ⚡ Core Features
- ✅ Detect firearms and improvised weapons in **images/videos**  
- ✅ Outputs annotated media with **bounding boxes**  
- ✅ Weapon alert system (triggers if a weapon is detected)  
- ✅ **Streamlit app** for uploading media and viewing results instantly  

---

## 🗂️ Dataset
- **Classes:** `Firearm`, `Improvised Weapons`, `No Weapon`  
- **Size:** ~1,500+ labeled images  
- **Annotations:** YOLO `.txt` format bounding boxes  
- **Notes:** Custom dataset collected & labeled manually  

---

## 🏋️ Model & Training
- **Architecture:** YOLOv8n (fine-tuned on custom dataset)  
- **Framework:** Ultralytics YOLOv8 + PyTorch  
- **Training Details:**  
  - Epochs: **50**  
  - Image Size: **640x640**  
  - Batch Size: system-dependent  
- **Metrics:** Evaluated on validation set  

---

## 📊 Weapon Detection Accuracy Metrics
Final results after **50 epochs of training**:  

- **Precision:** **36.8%**  
- **Recall:** **75.5%**  
- **mAP@0.5:** **79.6%**  
- **mAP@0.5:0.95:** *(expected ~55–65%)*  

---

## 📊 Model Performance

> **Important Note:**  
> The reported precision of the model is currently **36.8%**, which reflects the limitations of the available dataset.  
> Despite the low precision metric, the model **successfully detects weapons** in the test images and videos, demonstrating a working pipeline.  
> Users can further improve performance by training on a **larger and more diverse dataset**.

---

## 🎬 Video Analysis Pipeline
1. **Video Input** → Extract frames  
2. **YOLO Detection** → Detect weapons per frame  
3. **Output Generation** → Annotated video with bounding boxes + alerts  

---

## 🖥️ Streamlit Interface
- Upload an **image** or **video**  
- YOLO model runs detection on uploaded media  
- Outputs annotated **video/image** with bounding boxes  
- Displays **alert** if firearm/improvised weapon is detected  

---

## 📈 Results
- Successfully detected firearms and improvised weapons in test samples.  
- Bounding boxes drawn around detected threats.  

---

## ⚠️ Limitations
- Accuracy depends on dataset quality & size.  
- Rare/unusual improvised weapons may not be detected.  
- Real-time live stream detection not yet implemented.  

---

## 🚀 Future Scope
- Real-time webcam/CCTV detection.  
- Expand dataset with more weapon variations.  
- Multi-camera monitoring system.  
- Automated alert notifications (SMS, Email, Push).  

---

## 💻 Installation & Running (All-in-One)

```bash
# Clone the repository
git clone <YOUR_REPO_URL>
cd weapon-detection-system

# Create a virtual environment
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Train the model (optional)
yolo train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640

# Validate the model
yolo val model=runs/detect/train/weights/best.pt data=data.yaml

# Run the Streamlit app
streamlit run interface.py

# Run inference on a video
yolo detect predict model=runs/detect/train/weights/best.pt source="test.mp4"
