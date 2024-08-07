import cv2
import numpy as np
img = cv2.imread('apple.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5))/25
edges = cv2.Canny(gray, 100, 200)
texture = cv2.filter2D(gray, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Texture", texture)
cv2.waitKey(0)