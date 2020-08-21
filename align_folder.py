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

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

lines = load_images_from_folder('Images/Lines')
lines[0] = cv2.cvtColor(lines[0], cv2.COLOR_BGR2GRAY)
ocr.align_image(lines[0])
# for line in lines:
#     line = cv2.cvtColor(line, cv2.COLOR_BGR2GRAY)
#     line = ocr.align_image(line)
#
# os.chdir(r'C:\Users\Jenny\Desktop\AlignedLines')
#
# for i in range(0,len(lines)):
#     cv2.imshow(f"image{i}", lines[i])
#     file_name = f"line_{i}.jpg"
#     cv2.imwrite(f'{file_name}',lines[i])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
