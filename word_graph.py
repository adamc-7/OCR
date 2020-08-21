import os
import shutil
import tkinter as t
from tkinter import ttk, scrolledtext, messagebox
import numpy as np
import cv2
import ocr_functions as ocr
import imutils
from PIL import Image, ImageEnhance
from PIL import ImageOps
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.signal import savgol_filter

img = cv2.imread("Images/Lines/line_1.tif", 0)
counter = 0
averages = np.empty(img.shape[1])
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()

for col in img:
    averages[counter] = np.average(col)
    counter += 1

img = img.transpose()
# averages = savgol_filter(averages, 41, 5)
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(cols,averages)
ax.set_title("Average Pixel Value vs Column", fontsize=24)
ax.set_xlabel("Column", fontsize=14)
ax.set_ylabel("Average Pixel Value", fontsize=14)
plt.show()