import cv2
import numpy as np

img = cv2.imread('apple.jpg')
height, width, i = img.shape

rotated_matrix = cv2.getRotationMatrix2D((width//2, height//2),45,1)
scaled_matrix = np.float32([[1.5,0,0],[0,1.5,0]])
translated_matrix = np.float32([[1,0,100],[0,1,50]])

rotated_img = cv2.warpAffine(img, rotated_matrix, (width, height))
scaled_img = cv2.warpAffine(img, scaled_matrix, (int(1.5*width),int(1.5*height)))
translated_img = cv2.warpAffine(img, translated_matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", translated_img)
cv2.imshow("Scaled Image", scaled_img)
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)