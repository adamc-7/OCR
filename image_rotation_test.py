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
def calc_std(img):
    avg_array = np.empty(img.shape[0])
    counter = 0
    for row in img:
        avg_array[counter] = np.average(row)
        counter += 1
    return np.std(avg_array)

img = cv2.imread("Images/rotatednonbinary.tif",0)
img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# img = ocr.binary_img(img)
best_aligned = img
best_angle = 0

for i in range(-60,60):
    temp = imutils.rotate(img,i/10)
    print(calc_std(temp))
    if(calc_std(temp) > calc_std(best_aligned)):
        best_angle = i/10
        best_aligned = temp

print(f"Rotation Angle: {best_angle} degrees")
best_aligned = cv2.resize(best_aligned, (tuple(reversed(img.shape))))

cv2.imshow('original image', img)
cv2.imshow('modified image', best_aligned)
cv2.waitKey(0)
cv2.destroyAllWindows()

# os.chdir(r'C:\Users\Jenny\Desktop')
# cv2.imwrite(r"aligned-cropped-2.tif",best_aligned)
