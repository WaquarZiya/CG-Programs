import cv2
import numpy as np

img = cv2.imread('apple.jpg')
height, width, i = img.shape

up_left = img[0:height//2, 0:width//2]
up_right = img[0:height//2, width//2:width]
down_left = img[height//2:height, 0:width//2]
down_right = img[height//2:height, width//2:width]

canvas = np.zeros_like(img)

canvas[0:height//2, 0:width//2] = up_left
# canvas[0:height//2, width//2:width] = up_right
canvas[height//2:height, 0:width//2] = down_left
canvas[height//2:height, width//2:width] = down_right

cv2.imshow("Image Quadrants", canvas)
cv2.waitKey(0)