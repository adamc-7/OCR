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

img = cv2.imread("Images/Cropped/aligned-cropped-2.tif", 0)
counter = 0
rows = np.array(range(1,img.shape[0]+1))
goodaverages = np.empty(img.shape[0])
badaverages = np.empty(img.shape[0])
counter = 0
for row in img:
    goodaverages[counter] = np.average(row)
    badaverages[counter] = ocr.no_black_avg(row)
    counter += 1

img = ocr.binary_img(img)
fig, ax = plt.subplots(figsize=(15,9))
good_smoothed = savgol_filter(goodaverages, 41, 5)
bad_smoothed = savgol_filter(badaverages, 41, 5)
ax.plot(rows,good_smoothed,label="black not removed")
ax.plot(rows,bad_smoothed,label="black removed")
# ax.plot(rows,savgol_filter(badaverages, 21, 3),label="nonaligned")
plt.legend(loc="upper right")
ax.set_title("Average Pixel Value vs Row", fontsize=24)
ax.set_xlabel("Row", fontsize=14)
ax.set_ylabel("Average Pixel Value", fontsize=14)
plt.show()