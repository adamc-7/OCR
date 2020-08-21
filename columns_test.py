import os
import shutil
import tkinter as t
from tkinter import ttk, scrolledtext, messagebox
import numpy as np
import cv2
import imutils
import ocr_functions as ocr
from PIL import Image, ImageEnhance
from PIL import ImageOps
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import savgol_filter


img = cv2.imread("Images/Cropped/aligned-cropped-2.tif", 0)
counter = 0
standard_devs = np.empty(img.shape[1])
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()
for col in img:
    standard_devs[counter] = np.std(col)
    counter += 1

img = img.transpose()
standard_devs = savgol_filter(standard_devs, 41, 5)
derivatives = ocr.calc_derivatives(standard_devs)
line_cols = []
counter = 0
negative_slope_counter = 0
positive_slope_counter = 0
current_values = []
while counter < len(derivatives):
    if derivatives[counter] < 0:
        negative_slope_counter += 1
        counter += 1
        current_values.append(standard_devs[counter])
    else:
        if negative_slope_counter > 0.005*(img.shape[0]):
            while derivatives[counter] > 0 and counter < len(derivatives)-1:
                current_values.append(standard_devs[counter])
                positive_slope_counter += 1
                counter += 1
            counter -= positive_slope_counter
            if positive_slope_counter > 0.005*(img.shape[0]) and min(current_values) < 0.5*np.average(standard_devs):
                if(len(line_cols) == 0 or counter - line_cols[-1] > 0.02*(img.shape[1])):
                    line_cols.append(counter)
        negative_slope_counter = 0
        positive_slope_counter = 0
        current_values = []
        counter += 1

for i in line_cols:
     print(i)
     for j in range(0,img.shape[0]):
        img[j,i] = 0
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(r'C:\Users\Jenny\Desktop')
cv2.imwrite(r"column-line.jpg ",img)