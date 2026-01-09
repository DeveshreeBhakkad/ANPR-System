# Automatic Number Plate Recognition (ANPR)

This project implements a basic **Automatic Number Plate Recognition (ANPR)** system using **OpenCV** and **Tesseract OCR** in Python.

The current implementation follows a **contour-based approach** to detect the number plate region from a vehicle image and then applies OCR to extract the plate number.

---

## 🔧 Technologies Used
- Python
- OpenCV
- Tesseract OCR
- pytesseract

---


## 🧠 Working Overview
1. Read vehicle image
2. Convert image to grayscale and apply filtering
3. Detect edges using Canny edge detection
4. Find contours and approximate quadrilateral shapes
5. Select a potential number plate region
6. Crop the detected region
7. Extract text using Tesseract OCR
8. Display final ANPR output

---

## ⚠️ Current Limitations
- Uses a simple contour-based detection method
- May incorrectly detect non-plate rectangular regions
- Works best on clear, front-facing images
- Detection accuracy is limited for complex backgrounds

---

## 🚀 Future Improvements
- Improve plate localization using geometric filtering
- Use deep learning (YOLO/CNN) for robust plate detection
- Enhance OCR accuracy with preprocessing and validation

---

## 📌 Status
Project is under development. This version represents a **baseline ANPR implementation**.
