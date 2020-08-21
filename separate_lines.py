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


img = cv2.imread("Images/Cropped/aligned-cropped-1.tif", 0)
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
        line_rows.append(i)

# for i in line_rows:
#      for j in range(0,img.shape[1]):
#         img[i,j] = 255
line_rows.append(img.shape[0]-1)
lines = []
# os.chdir(r'C:\Users\Jenny\Desktop\CroppedLines')
for i in range(0,len(line_rows)-1):
    lines.append(img[line_rows[i]:line_rows[i+1],0:img.shape[1]])
    cv2.imshow(f"line{i}", lines[i])
    # file_name = f"line_{i}.jpg"
    # cv2.imwrite(f'{file_name}',lines[i])
cv2.waitKey(0)
cv2.destroyAllWindows()

