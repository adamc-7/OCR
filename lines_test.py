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


img = cv2.imread("Images/Cropped/edges.jpg", 0)
counter = 0
averages = np.empty(img.shape[0])
rows = np.array(range(1,img.shape[0]+1))
# img = ocr.binary_img(img)
for row in img:
    averages[counter] = np.average(row)
    counter += 1

averages = savgol_filter(averages, 41, 5)
derivatives = ocr.calc_derivatives(averages)
line_rows = [0]
for i in range(0,len(derivatives)-1):
    if derivatives[i] > 0 and derivatives[i+1] < 0:
        print(i)
        if i-line_rows[-1] > 0.01*img.shape[0]:
            line_rows.append(i)
print(img.shape[0],img.shape[1])
for i in line_rows:
    for j in range(0,img.shape[1]):
        img[i,j] = 255
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# os.chdir(r'C:\Users\Jenny\Desktop')
# cv2.imwrite(r"image-with-lines.jpg",img)
