import cv2
import easyocr
import re

reader = easyocr.Reader(['en'], gpu=False)

# ---------------- Load image ----------------
img = cv2.imread("Images/img1.jpg")
if img is None:
    raise FileNotFoundError("Image not found")

# ---------------- Preprocessing ----------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# ---------------- Find contours ----------------
contours, _ = cv2.findContours(
    edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

plate_cnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if 4 <= len(approx) <= 8:
        x, y, w, h = cv2.boundingRect(approx)
        if 2 < w / float(h) < 6 and cv2.contourArea(c) > 2000:
            plate_cnt = approx
            break

# ---------------- Fallback logic ----------------
if plate_cnt is None:
    print("Plate contour not found. Using full image for OCR.")
    plate_img = img.copy()
else:
    x, y, w, h = cv2.boundingRect(plate_cnt)
    plate_img = img[y:y+h, x:x+w]
    cv2.drawContours(img, [plate_cnt], -1, (0, 255, 0), 3)

# ---------------- OCR (spatial sorting) ----------------
result = reader.readtext(plate_img)
result = sorted(result, key=lambda r: r[0][0][0])

raw_text = " ".join([r[1] for r in result])
print("Raw OCR:", raw_text)

#

# ---------------- Show result ----------------
cv2.putText(
    img,
    final_plate,
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.2,
    (0, 255, 0),
    3
)

cv2.imshow("ANPR Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
