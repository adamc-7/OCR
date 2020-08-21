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
from scipy.signal import savgol_filter,medfilt


img = cv2.imread("Images/Cropped/aligned-cropped-1.tif", 0)
img = img[0:img.shape[0],0:int(img.shape[1]/2)]
counter = 0
averages = np.empty(img.shape[0])
rows = np.array(range(1,img.shape[0]+1))

for row in img:
    averages[counter] = ocr.no_black_avg(row)
    counter += 1
print(np.std(averages))
smoothed_averages = savgol_filter(averages, 23, 3)
# medfilt_averages = medfilt(averages,3)
# img = ocr.binary_img(img)
derivatives = ocr.calc_derivatives(smoothed_averages)
line_rows = []

for i in range(0,len(derivatives)-1):
    if derivatives[i] > 0 and derivatives[i+1] < 0:
        # print(i)
        line_rows.append(i+1)

# for i in line_rows:
#      # print(ocr.no_black_avg(img[i]))




counter = 0
standard_devs = np.empty(img.shape[0])
cols = np.array(range(1,img.shape[0]+1))

for row in img:
    standard_devs[counter] = np.std(row)
    counter += 1

standard_devs = savgol_filter(standard_devs, 23, 3)

plt.figure(1)
# plt.plot(rows,averages,label='no smoothing')
plt.plot(rows,smoothed_averages,label='original smoothing')
# plt.plot(rows,medfilt_averages,label='medfilt')
# for line in line_rows:
#     plt.axvline(line, color='red')
plt.xlabel("Row", fontsize=14)
plt.ylabel("Average Pixel Value", fontsize=14)
plt.title("Average Pixel Value vs Row", fontsize=24)
# plt.legend(loc ='upper right')
# plt.figure(2)
# plt.plot(cols,standard_devs)
# for line in line_rows:
#     plt.axvline(line, color='red')
# plt.xlabel("Row", fontsize=14)
# plt.ylabel("Standard Deviation", fontsize=14)
# plt.title("Standard Deviation vs Row", fontsize=24)
os.chdir(r'C:\Users\Jenny\Desktop')
plt.savefig("line-graph.png",bbox_inches='tight')

plt.show()