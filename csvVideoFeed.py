import cv2
import csv
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class videoToCSVConverter:
    def CSVConverter(width, height):
        vc = cv2.VideoCapture(0)
        for _ in range(20):
            vc.read()
        rval, frame = vc.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.resize(frame, (width, height))
        np_array = np.array(frame)
        with open("videoFeed.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for row in np_array:
                writer.writerow(row)
videoToCSVConverter.CSVConverter(1, 2)
