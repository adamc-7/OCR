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
cols = np.array(range(1,img.shape[1]+1))
img = img.transpose()

top_sum = 0
bottom_sum = 0
midpoint1 = 0
midpoint2 = 0
midpoint_list1 = []
midpoint_list2 = []
for col in img:
    minimum_difference = 10000
    for i in range(0,img.shape[1]):
        top_sum = sum(col[:i])
        bottom_sum = sum(col[i:])
        if (abs(top_sum-bottom_sum) < minimum_difference):
            midpoint1 = i
            minimum_difference = abs(top_sum-bottom_sum)
    midpoint2 = (col*np.arange(len(col))).sum()/col.sum()
    midpoint_list1.append(midpoint1)
    midpoint_list2.append(midpoint2)


img = img.transpose()
midpoint_list1 = savgol_filter(midpoint_list1, 41, 3)
midpoint_list2 = savgol_filter(midpoint_list2, 41, 3)
derivatives1 = ocr.calc_derivatives(midpoint_list1)
derivatives2 = ocr.calc_derivatives(midpoint_list2)
line_cols1 = []
line_cols2 = []

# for i in range(0,len(derivatives1)-1):
#     if abs(derivatives1[i] - derivatives1[i+1]) > 0.2:
#         if derivatives1[i] > 0 and derivatives1[i+1] < 0:
#             print(derivatives1[i],derivatives1[i+1])
#             line_cols1.append(i)

# for i in range(0,len(midpoint_list1)):
#     if(midpoint_list1[i] > 40):
#         line_cols1.append(i)

# for j in line_cols1:
#     for i in range(0,img.shape[0]):
#         img[i,j] = 255

# for i in range(0,len(derivatives2)-1):
#     if abs(derivatives2[i] - derivatives2[i+1]) > 0.15:
#         if derivatives2[i] > 0 and derivatives2[i+1] < 0:
#             print(derivatives2[i],derivatives2[i+1])
#             line_cols2.append(i)

# for i in range(0,len(midpoint_list2)):
#     if(midpoint_list2[i] > 40):
#         line_cols2.append(i)

# for j in line_cols2:
#     for i in range(0,img.shape[0]):
#         img[i,j] = 255
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()