import cv2
img = cv2.imread('apple.jpg')

gaussian = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 10, 100, 100)

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Bilateral Filter", bilateral)
cv2.imshow("Median Blur", median)
cv2.waitKey(0)