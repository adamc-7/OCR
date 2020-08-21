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

img = cv2.imread("Images/Cropped/aligned-cropped-1.tif", 0)
# img = ocr.align_image(img)
cols = ocr.separate_columns(img)
lines = []
words = []

# for i in range(len(cols)):
#     lines.append(ocr.separate_lines(cols[i]))
#
# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         # cv2.imshow(f"{i} {j}",lines[i][j])
#         words.append(ocr.separate_words(lines[i][j]))
#
# for i in range(len(words)):
#     for j in range(len(words[i])):
#         # for k in range(len(words[i][j])):
#         # print(f"j:{j} k:{k}")
#         cv2.imshow(f' line{i} word {j}',words[i][j])
# print(len(words))
# print(len(words[0]))
# print(len(words[0][0]))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# for i in range(len(cols)):
#     # cv2.imshow(f'col {i}',cols[i])
#     temp = ocr.separate_lines(cols[i])
#     for line in temp:
#          lines.append(line)
#
# for i in range(len(lines)):
#     words.append(ocr.separate_words(lines[i]))
#
# os.chdir(r'C:\Users\Jenny\Desktop\Aligned-1-Words')
# for i in range(len(words)):
#     if i<10:
#         dirName = fr'C:\Users\jenny\Desktop\Aligned-1-Words\Line0{i}-Words'
#     else:
#         dirName = fr'C:\Users\jenny\Desktop\Aligned-1-Words\Line{i}-Words'
#     try:
#         # Create target Directory
#         os.mkdir(dirName)
#         print("Directory ", dirName, " Created ")
#     except FileExistsError:
#         print("Directory ", dirName, " already exists")
#     os.chdir(dirName)
#     for j in range(len(words[i])):
#         # cv2.imshow(f'line{i} word {j}',words[i][j])
#         if i < 10 and j < 10:
#             file_name = f'line0{i}-word0{j}.jpg'
#         elif i < 10 and j >= 10:
#             file_name = f'line0{i}-word{j}.jpg'
#         elif i >= 10 and j < 10:
#             file_name = f'line{i}-word0{j}.jpg'
#         else:
#             file_name = f'line{i}-word{j}.jpg'
#         cv2.imwrite(f'{file_name}',words[i][j])
#         # print(f'i:{i} j:{j}')

cv2.waitKey(0)
cv2.destroyAllWindows()

# img = cv2.resize(img,(img.shape[1]*2,img.shape[0]*2))
# img = ocr.binary_img(img)
# img = cv2.Canny(img,100,200)
# print(ocr.transcribe(img))
# print("------------------------------------------------------------------")
# print(ocr.translate(ocr.transcribe(img)))
# print("------------------------------------------------------------------")
# for line in lines:
#     print(ocr.transcribe(line))
# print("------------------------------------------------------------------")
# for line in lines:
#     try:
#         print(ocr.translate(ocr.transcribe(line)))
#     except:
#         print('',end='')
# print("------------------------------------------------------------------")
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
rootdir = r'C:\Users\Jenny\Desktop\Aligned-1-Words'
os.chdir(r'C:\Users\Jenny\Desktop\Aligned-1-Words')
# print(os.listdir(rootdir))
# for line_folder in os.listdir(rootdir):
#     word_images = ocr.load_images_from_folder(line_folder)
#     for word in word_images:
#         print(ocr.transcribe(word),' ',end = '')
#     print()
# print("------------------------------------------------------------------")
for line_folder in os.listdir(rootdir):
    word_images = ocr.load_images_from_folder(line_folder)
    for word in word_images:
        try:
            print(ocr.transcribe(word,'lat'), ' ', end='')
        except:
            print('',end='')
    print()
        # print(ocr.transcribe(os.path.join(subdir, file)))

