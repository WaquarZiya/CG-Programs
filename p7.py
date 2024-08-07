import cv2
import numpy as np
img = cv2.imread('apple.jpg')
height, width, i = img.shape

canvas = np.zeros_like(img)
canvas[0:height//2, 0:width//2] = img[0:height//2, 0:width//2]
# canvas[0:height//2, width//2:width] = img[0:height//2, width//2:width]
canvas[height//2:height, 0:width//2] = img[height//2:height, 0:width//2]
canvas[height//2:height, width//2:width] = img[height//2:height, width//2:width]

cv2.imshow("Image Quadrants", canvas)
cv2.waitKey(0)