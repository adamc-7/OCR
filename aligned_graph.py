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
from datetime import datetime
from scipy.signal import savgol_filter



goodimg = cv2.imread("Images/alignedimage.tif", 0)
badimg = cv2.imread("Images/nonalignedimage.tif", 0)
counter = 0
rows = np.array(range(1,goodimg.shape[0]+1))
goodaverages = np.empty(goodimg.shape[0])
badaverages = np.empty(badimg.shape[0])
counter = 0
for goodrow,badrow in zip(goodimg,badimg):
    goodaverages[counter] = np.average(goodrow)
    badaverages[counter] = np.average(badrow)
    counter += 1

fig, ax = plt.subplots(figsize=(15,9))
good_smoothed = savgol_filter(goodaverages, 41, 5)
bad_smoothed = savgol_filter(badaverages, 41, 5)
ax.plot(rows,good_smoothed,label="deskewed")
ax.plot(rows,bad_smoothed,label="original (skewed)")
# ax.plot(rows,savgol_filter(badaverages, 21, 3),label="nonaligned")
plt.legend(loc="upper right")
ax.set_title("Average Pixel Value vs Row", fontsize=24)
ax.set_xlabel("Row", fontsize=14)
ax.set_ylabel("Average Pixel Value", fontsize=14)
os.chdir(r'C:\Users\Jenny\Desktop')
plt.savefig('aligned_graph.png')
plt.show()

