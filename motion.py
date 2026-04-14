import cv2
import config

def detect_motion(frame1, frame2):
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Rauschen reduzieren
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

# Thresholding
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

# Bewegung = Anzahl weißer Pixel
    motion_value = cv2.countNonZero(thresh)

    return motion_value > config.THRESHOLD
