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

img = cv2.imread("Images/rotatedText.png", 0)
img = ocr.binary_img(img)
img = imutils.rotate(img,-20)
# img = img[10:img.shape[0]-10,0:1084]
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()
top_sum = 0
bottom_sum = 0
midpoint = 0
midpoint_list = []
for col in img:
    minimum_difference = 10000
    for i in range(0,img.shape[1]):
        top_sum = sum(col[:i])
        bottom_sum = sum(col[i:])
        if (abs(top_sum-bottom_sum) < minimum_difference):
            midpoint = i
            minimum_difference = abs(top_sum-bottom_sum)
    midpoint_list.append(midpoint)

img = img.transpose()
midpoint_list = savgol_filter(midpoint_list, 41, 3)
# curve_fit = np.polyfit(cols,midpoint_list1,3)

fig, ax = plt.subplots(figsize=(15,9))
ax.plot(cols,midpoint_list)
ax.set_title("Midpoint vs Column", fontsize=24)
ax.set_xlabel("Column", fontsize=14)
ax.set_ylabel("Midpoint", fontsize=14)
trend = np.polyfit(cols,midpoint_list,3)
print(trend)
trendpoly = np.poly1d(trend)
plt.plot(cols,trendpoly(cols))
plt.show()
img = img.transpose()
for i in range(0,img.shape[0]):
    row = int(trend[0]*(i**3) + trend[1]*(i**2) + trend[2]*i + trend[3])
    if i == 0:
        x1 = 0
        y1 = row
        print(y1)
    if i == img.shape[0]-1:
        x2 = img.shape[0]-1
        y2 = row
        print(y2)
    img[i,img.shape[1]-row] = 0
img = img.transpose()
slope = (y1-y2)/(x1-x2)
angle = np.arctan(slope)*(180/np.pi)
print(angle)
# img = imutils.rotate(img,angle)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
