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
from matplotlib.ticker import MaxNLocator
from datetime import datetime


pixel = []
labels = ["reg-c-3C10.tif","reg-c-OC5.tif","reg-c-3C8.tif","reg-c-3C11.tif","reg-c-CC15.tif"]
img1 = cv2.imread("Images/reg-c-3C10.tif",0)
img2 = cv2.imread("Images/reg-c-OC5.tif",0)
img3 = cv2.imread("Images/reg-c-3C8.tif",0)
img4 = cv2.imread("Images/reg-c-3C11.tif",0)
img5 = cv2.imread("Images/reg-c-CC15.tif",0)
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # cv2.circle(img1,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img1)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        cv2.destroyAllWindows()
        pixel = [mouseX,mouseY]
        # print(mouseX, mouseY)
        images = [img1, img2, img3, img4, img5]
        x = np.array(range(1, len(images) + 1))
        pixel_values = []

        for img in images:
            pixel_values.append(img[pixel[0], pixel[1]])

        fig, ax = plt.subplots(figsize=(15, 9))
        ax.plot(x, pixel_values)
        ax.set_xlabel("Image Name", fontsize=14)
        ax.set_ylabel(f"Pixel Value at {pixel}", fontsize=14)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xticks(x,labels)
        plt.show()



