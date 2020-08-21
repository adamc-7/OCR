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
import pytesseract
from googletrans import Translator
from os.path import expanduser
# os.chdir(r'C:\Users\Jenny\Desktop')
img = cv2.imread('Images/rotatednonbinary.tif',0)
line = cv2.imread('Images/Lines/line_1.tif',0)
img = cv2.resize(img,(0,0),fx=3,fy=3)
line = cv2.resize(line,(0,0),fx=3,fy=3)
# word = cv2.imread('Images/line2-words/word_7.jpg',0)
word = cv2.imread(r'C:\Users\jenny\Desktop\Aligned-1-Words\Line23-Words\line23-word04.jpg',0)

# word = ocr.binary_img(word)

word = cv2.resize(word,(0,0),fx=3,fy=3)
# word = cv2.threshold(word,145, 255, cv2.THRESH_BINARY)[1]
# word = cv2.resize(word,(word.shape[1]*2,word.shape[0]*2))
thresh = cv2.threshold(word,155, 255, cv2.THRESH_BINARY)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
result = 255-close
cv2.imshow('thresh', thresh)
cv2.imshow('close', close)
cv2.imshow('result', result)


# print(ocr.transcribe(img))
# print("------------------------------------------------------------------")
# print(ocr.transcribe(line))
# print("------------------------------------------------------------------")
print(ocr.transcribe(word,'enm'))
print(ocr.transcribe(thresh,'enm'))
print(ocr.transcribe(close,'enm'))
print(ocr.transcribe(result,'enm'))
print(ocr.transcribe(word))
print(ocr.transcribe(thresh))
print(ocr.transcribe(close))
print(ocr.transcribe(result))
cv2.imshow('image',word)
# cv2.imwrite('arbor.jpg',word)
cv2.waitKey(0)
cv2.destroyAllWindows()