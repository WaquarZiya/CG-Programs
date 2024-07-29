import cv2
img = cv2.imread('apple.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()

cv2.drawContours(contour_img, contours, -1, (255,0,0), 2)
cv2.imshow("Original Image", img)
cv2.imshow("Contour Image", contour_img)
cv2.waitKey(0)