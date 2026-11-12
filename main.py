import cv2
import csv
import numpy as np
vcCount = 0
width = 256
height = 128
while True:
    if vcCount!=1:
        vc = cv2.VideoCapture(0)
        vcCount+=1
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    np_array = cv2.resize(frame, (width, height))
    cv2.imshow('Cool Skibidi Sigma App Name', frame)
    with open("videoFeed.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for row in np_array:
            writer.writerow(row)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
