import cv2
import ctypes
import pytesseract

# -------- Center window --------
def center_window(win_name, img):
    h, w = img.shape[:2]
    user32 = ctypes.windll.user32
    screen_w = user32.GetSystemMetrics(0)
    screen_h = user32.GetSystemMetrics(1)

    x = max(0, (screen_w - w) // 2)
    y = max(0, (screen_h - h) // 2)

    cv2.moveWindow(win_name, x, y)

# -------- Read image --------
img = cv2.imread('Images/img1.webp')
if img is None:
    raise FileNotFoundError("Image not found")

cv2.namedWindow('Car Image', cv2.WINDOW_NORMAL)
cv2.imshow('Car Image', img)
center_window('Car Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------- Preprocessing --------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)
cv2.imshow('Gray Image', gray)
center_window('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Edges', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------- Find contours --------
contours, _ = cv2.findContours(
    edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
)

contours = sorted(contours, key=cv2.contourArea, reverse=True)

plate_cnt = None

for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        plate_cnt = approx
        break

if plate_cnt is None:
    raise Exception("Number plate contour not found")

# -------- Crop plate --------
x, y, w, h = cv2.boundingRect(plate_cnt)
plate_img = gray[y:y+h, x:x+w]

cv2.namedWindow('Number Plate', cv2.WINDOW_NORMAL)
cv2.imshow('Number Plate', plate_img)
center_window('Number Plate', plate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# -------- OCR --------
pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

text = pytesseract.image_to_string(
    plate_img, config='--psm 8'
)

print('Detected Number Plate:', text)

# -------- Final output --------
cv2.drawContours(img, [plate_cnt], -1, (0, 255, 0), 3)
cv2.putText(
    img, text.strip(), (x, y - 10),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
)

cv2.namedWindow('ANPR Output', cv2.WINDOW_NORMAL)
cv2.imshow('ANPR Output', img)
center_window('ANPR Output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
