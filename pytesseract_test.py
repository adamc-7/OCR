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
import pytesseract
from pytesseract import Output



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
words = ocr.load_images_from_folder(r'C:\Users\Jenny\Desktop\Aligned-1-Words\Line11-Words')
# img = ocr.binary_img(img)
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# img = lines[1]
# print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_string(img,lang='lat'))
# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
for word in words:
    word = cv2.resize(word, (0, 0), fx=3, fy=3)
    # word = cv2.threshold(word,145, 255, cv2.THRESH_BINARY)[1]
    # word = cv2.resize(word,(word.shape[1]*2,word.shape[0]*2))
    thresh = cv2.threshold(word, 145, 255, cv2.THRESH_BINARY)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    result = 255 - close
    # print(ocr.transcribe(word, 'lat+enm'),end= ' ')
    print(ocr.transcribe(thresh, 'lat+enm'),end= ' ')
    # print(ocr.transcribe(close, 'lat+enm'),end= ' ')
    # print(ocr.transcribe(result, 'lat+enm'),end= ' ')

# full_image = cv2.imread('Images/Cropped/aligned-cropped-1.tif',0)
# print("-----------------------------------------------------------------\n\n\n\n\n\n\n")
# print(pytesseract.image_to_string(full_image,lang='eng'))
# cv2.imshow('full img',full_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# n_boxes = len(d['level'])
# for i in range(n_boxes):
#     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()