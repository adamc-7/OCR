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
standard_devs = np.empty(img.shape[1])
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()

for col in img:
    standard_devs[counter] = np.std(col)
    counter += 1

img = img.transpose()
standard_devs = savgol_filter(standard_devs, 45, 5)
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(cols,standard_devs)
ax.set_title("Standard Deviation vs Column", fontsize=24)
ax.set_xlabel("Column", fontsize=14)
ax.set_ylabel("Standard Deviation", fontsize=14)
os.chdir(r'C:\Users\Jenny\Desktop')
plt.savefig("word-graph.png",bbox_inches='tight')
plt.show()
