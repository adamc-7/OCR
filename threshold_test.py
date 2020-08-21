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

img = cv2.imread("Images/Lines/line_1.tif", 0)
values = []
for x in range(len(img)):
    for y in range(len(img[0])):
        values.append(img[x,y])
average = ocr.no_black_avg(values)
print(average)
for x in range(len(img)):
    for y in range(len(img[0])):
        if (img[x, y] < 80  or img[x, y] > 90):
            img[x, y] = 0
        else:
            img[x, y] = 255
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()