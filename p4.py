import cv2
import numpy as np

screen = np.ones([650, 1300, 3])
obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]])

translated_matrix = np.array([[1, 0, 100], [0, 1, 50]])
rotated_matrix = cv2.getRotationMatrix2D([150, 150], 45, 1)
scaled_matrix = np.array([[1.5, 0, 0], [0, 1.5, 0]])

translated_obj = np.array([np.dot(translated_matrix, [x, y, 1])[:2] for x, y in obj_points], dtype=np.int32)
rotated_obj = np.array([np.dot(rotated_matrix, [x, y, 1])[:2] for x, y in translated_obj], dtype=np.int32)
scaled_obj = np.array([np.dot(scaled_matrix, [x, y, 1])[:2] for x, y in rotated_obj], dtype=np.int32)

cv2.polylines(screen, [obj_points], True, (0,0,0), 2)
cv2.polylines(screen, [translated_obj], True, (255,0,0), 2)
cv2.polylines(screen, [rotated_obj], True, (0,255,0), 2)
cv2.polylines(screen, [scaled_obj], True, (0,0,255),2)

cv2.imshow("2D transformation", screen)
cv2.waitKey(0)