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


img = cv2.imread("Images/reg-c-3C10.tif", 0)
for x in range(0,4):
    counter = 0
    averages = np.empty(img.shape[0])
    rows = np.array(range(1,img.shape[0]+1))

    for row in img:
        start = int((img.shape[1]/4) * x)
        end = int((img.shape[1]/4)*(x+1))
        print(start,end)
        averages[counter] = ocr.no_black_avg(row[start:end+1])
        counter += 1

    averages = savgol_filter(averages, 41, 5)
    # img = ocr.binary_img(img)
    derivatives = ocr.calc_derivatives(averages)
    line_rows = []

    for i in range(0,len(derivatives)-1):
        if derivatives[i] > 0 and derivatives[i+1] < 0:
            line_rows.append(i)

    for i in line_rows:
        for j in range(start,end):
            img[i,j] = 0
img = ocr.binary_img(img)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for r in range(len(img)):
#     white_counter = 0
#     for c in range(len(img[0])):
#         if(img[r,c]):
#             white_counter += 1
#     averages[r] = white_counter/(1084-white_counter)
# averages = savgol_filter(averages, 51, 5)

# for x in range(len(img)):
#     for y in range(len(img[0])):
#         img[x, y] = 0