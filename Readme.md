# 🚘 Automatic Number Plate Recognition (ANPR)

> *“Engineering is not about building perfect systems — it’s about understanding limitations and making conscious design decisions.”*

---

## 📌 Project Overview

This project is a **learning-focused implementation of Automatic Number Plate Recognition (ANPR)** designed to explore how classical computer vision and OCR techniques behave on **real-world Indian vehicle number plates**.

The goal of this project is **not to claim an industry-grade system**, but to:
   - understand the complete ANPR pipeline,
   - experiment with real-world constraints,
   - and learn why production systems rely on deep learning–based approaches.

---

## 🎯 What This Project Does

✔ Detects number plate regions using **OpenCV contour-based techniques**  
✔ Performs text recognition using **EasyOCR**  
✔ Applies **post-processing** to clean OCR output  
✔ Handles real-world challenges such as:<br>
   - Indian plate fonts<br>
   - logos like `IND`<br>
   - borders and uneven spacing<br>
   - partial detection failures  <br>

✔ Displays the detected plate and recognized text on the image  

---

## 🧠 Why This Project Exists

While ANPR is a widely used application, implementing it on **Indian number plates** highlights important challenges:
   - OCR struggles with stylized fonts
   - plate borders interfere with detection
   - classical CV methods fail on many real-world cases

This project helped me **bridge the gap between academic approaches and real-world engineering realities**.

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV** – image preprocessing and contour detection
- **EasyOCR** – deep learning–based OCR
- **NumPy** – numerical operations
- **PyTorch** – backend used by EasyOCR

---

## ⚙️ Pipeline Explanation

### 1️⃣ Image Preprocessing
- Convert image to grayscale
- Apply bilateral filtering to reduce noise
- Detect edges using Canny edge detection

### 2️⃣ Plate Localization
- Find contours in the image
- Filter contours based on:
  - shape
  - aspect ratio
  - area
- Use fallback OCR when contour detection fails

### 3️⃣ OCR (Text Recognition)
- Extract text using EasyOCR
- Sort OCR results spatially (left → right)

### 4️⃣ Post-Processing
- Remove noise such as `IND` and special characters
- Apply regex-based formatting for Indian number plates

---

## ⚠️ Known Limitations (Intentionally Documented)

This project clearly acknowledges its limitations:

- OCR may misinterpret characters due to **Indian plate fonts**
    - Example: `W` detected as `N`
- Trailing characters close to plate borders may be missed
- Contour-based detection fails for:
    - rounded plates
    - broken or merged boundaries
- Stock images with watermarks introduce OCR noise

These limitations demonstrate **why real-world ANPR systems rely on deep learning–based detection models**.

---

## 🎓 Key Learnings

- Classical computer vision techniques are fragile in real-world scenarios
- OCR accuracy depends heavily on font design and spacing
- Robust systems require fallback strategies
- Understanding limitations is more important than forcing accuracy
- Scope control is an important engineering skill

---

## 🚀 Future Improvements (Not Implemented)

The following improvements were intentionally left out to keep the project aligned with my learning scope:

- YOLO-based number plate detection
- Character-level OCR models (CRNN)
- Video-based multi-frame aggregation
- Confidence scoring and validation

---

## 📁 Project Structure

```bash
ANPR-System/
│
├── Images/
│ ├── img1.jpg
│ ├── img2.jpg
│ └── img3.webp
│
├── auto_num_detect.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🧩 Final Note

This project represents a **baseline ANPR implementation** created to learn, experiment, and understand real-world constraints in computer vision and OCR.

It reflects:
  - honest engineering decisions
  - practical debugging
  - and a learning-first mindset

---

📌 *Built as part of hands-on exploration in Computer Vision and OCR.*
