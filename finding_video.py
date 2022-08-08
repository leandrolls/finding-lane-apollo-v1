import cv2
import numpy as np
from utils import image
from utils import coordinates


cap = cv2.VideoCapture("video_test.mp4")
while cap.isOpened():
    _, frame = cap.read()
    canny_image = image.canny(frame)
    cropped = coordinates.region(canny_image)
    lines = cv2.HoughLinesP(cropped, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=10500)
    average_lines = coordinates.average_slope_intercept(frame, lines)
    line_image = image.display(frame, average_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result", combo_image)
    cv2.waitKey(1)
