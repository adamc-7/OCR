import os
import shutil
import tkinter as t
from tkinter import ttk, scrolledtext, messagebox
import numpy as np
import cv2
import imutils
from PIL import Image, ImageEnhance
from PIL import ImageOps
import matplotlib.pyplot as plt
import ocr_functions as ocr
from datetime import datetime
from scipy.signal import savgol_filter


img = cv2.imread("Images/TypedLines/line_4.jpg", 0)
counter = 0
averages = np.empty(img.shape[1])
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()

for col in img:
    averages[counter] = np.average(col)
    counter += 1

img = img.transpose()
averages = savgol_filter(averages, 41, 5)
img = ocr.binary_img(img)
derivatives = ocr.calc_derivatives(averages)
line_cols = []

for i in range(0,len(derivatives)-1):
    # if abs(derivatives[i] - derivatives[i+1]) > 0:
        if derivatives[i] > 0 and derivatives[i+1] < 0:
            print(derivatives[i],derivatives[i+1])
            line_cols.append(i)

for j in line_cols:
    for i in range(0,img.shape[0]):
        img[i,j] = 255
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()