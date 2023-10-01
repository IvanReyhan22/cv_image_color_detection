import cv2
import numpy as np

image = cv2.imread("objek.jpeg")
cv2.imshow('original', image)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# warna yang ingin di deteksi format BGR
color = np.uint8([[[0, 255, 255]]]) # kuning
# color = np.uint8([[[0, 255, 0]]]) # hijau
# color = np.uint8([[[0, 0, 255]]]) # merah
# color = np.uint8([[[255, 0, 0]]]) # biru

hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)

hue = hsv_color[0][0][0]

if hue >= 165:  
    lower_color = np.array([hue - 10, 100, 100])
    upper_color = np.array([180, 255, 255])
elif hue <= 15:
    lower_color = np.array([0, 100, 100])
    upper_color = np.array([hue + 10, 255, 255])
else:
    lower_color = np.array([hue - 10, 100, 100])
    upper_color = np.array([hue + 10, 255, 255])

mask = cv2.inRange(hsv_image, lower_color, upper_color)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('detection', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
