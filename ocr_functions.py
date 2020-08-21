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
from datetime import datetime
from scipy.signal import savgol_filter
import pytesseract
from googletrans import Translator

def no_black_avg(arr):
    total = 0
    black_count = 0
    for x in arr:
        if x != 0:
            total += x
        else:
            black_count += 1
    if black_count == len(arr):
        return
    else:
        return total / (len(arr) - black_count)

def binary_img(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            if (img[x, y] < 65):
                img[x, y] = 255
            else:
                img[x, y] = 0
    return img

def calc_derivatives(y):
    dx = 1
    dy = np.diff(y)/dx
    return dy

def align_image(img):
    def calc_std(img):
        avg_array = np.empty(img.shape[0])
        counter = 0
        for row in img:
            avg_array[counter] = np.average(row)
            counter += 1
        return np.std(avg_array)
    best_aligned = img
    best_angle = 0

    for i in range(-50, 50):
        temp = imutils.rotate(img, i / 10)
        print(calc_std(temp))
        if (calc_std(temp) > calc_std(best_aligned)):
            best_angle = i / 10
            best_aligned = temp

    print(f"Rotation Angle: {best_angle} degrees")
    best_aligned = cv2.resize(best_aligned, (tuple(reversed(img.shape))))
    return best_aligned

def draw_lines(img):
    counter = 0
    averages = np.empty(img.shape[0])
    rows = np.array(range(1, img.shape[0] + 1))
    # img = ocr.binary_img(img)
    for row in img:
        averages[counter] = np.average(row)
        counter += 1

    averages = savgol_filter(averages, 41, 5)
    derivatives = calc_derivatives(averages)
    line_rows = [0]
    for i in range(0, len(derivatives) - 1):
        if derivatives[i] > 0 and derivatives[i + 1] < 0:
            if i - line_rows[-1] > 0.01 * img.shape[0]:
                print(i)
                line_rows.append(i)

    for i in line_rows:
        for j in range(0, img.shape[1]):
            img[i, j] = 255
    return img

def draw_word_lines(img):
    counter = 0
    standard_devs = np.empty(img.shape[1])
    img = img.transpose()

    for col in img:
        standard_devs[counter] = np.std(col)
        counter += 1

    img = img.transpose()
    standard_devs = savgol_filter(standard_devs, 41, 5)
    derivatives = calc_derivatives(standard_devs)
    line_cols = []
    counter = 0
    negative_slope_counter = 0
    positive_slope_counter = 0
    current_values = []
    while counter < len(derivatives):
        if derivatives[counter] < 0:
            negative_slope_counter += 1
            counter += 1
            current_values.append(standard_devs[counter])
        else:
            if negative_slope_counter > 0.15 * (img.shape[0] - 20):
                while derivatives[counter] > 0 and counter < len(derivatives) - 1:
                    current_values.append(standard_devs[counter])
                    positive_slope_counter += 1
                    counter += 1
                counter -= positive_slope_counter
                if positive_slope_counter > 0.15 * (img.shape[0] - 20) and min(current_values) < 0.8 * np.average(
                        standard_devs):
                    print(negative_slope_counter, positive_slope_counter)
                    if (len(line_cols) == 0 or counter - line_cols[-1] > 0.02 * (img.shape[1])):
                        line_cols.append(counter)
            negative_slope_counter = 0
            positive_slope_counter = 0
            current_values = []
            counter += 1

    # for i in range(0,len(standard_devs)):
    #     if(standard_devs[i] < 16):
    #         line_cols.append(i)

    for j in line_cols:
        for i in range(0, img.shape[0]):
            img[i, j] = 255
    return img
def separate_columns(img):
    counter = 0
    standard_devs = np.empty(img.shape[1])
    img = img.transpose()
    for col in img:
        standard_devs[counter] = np.std(col)
        counter += 1

    img = img.transpose()
    standard_devs = savgol_filter(standard_devs, 41, 5)
    derivatives = calc_derivatives(standard_devs)
    line_cols = [0]
    counter = 0
    negative_slope_counter = 0
    positive_slope_counter = 0
    current_values = []
    while counter < len(derivatives):
        if derivatives[counter] < 0:
            negative_slope_counter += 1
            counter += 1
            current_values.append(standard_devs[counter])
        else:
            if negative_slope_counter > 0.005 * (img.shape[0]):
                while derivatives[counter] > 0 and counter < len(derivatives) - 1:
                    current_values.append(standard_devs[counter])
                    positive_slope_counter += 1
                    counter += 1
                counter -= positive_slope_counter
                if positive_slope_counter > 0.005 * (img.shape[0]) and min(current_values) < 0.5 * np.average(
                        standard_devs):
                    if (len(line_cols) == 0 or counter - line_cols[-1] > 0.02 * (img.shape[1])):
                        line_cols.append(counter)
            negative_slope_counter = 0
            positive_slope_counter = 0
            current_values = []
            counter += 1
    line_cols.append(img.shape[1] - 1)
    os.chdir(r'C:\Users\Jenny\Desktop\Words')
    cols = []
    for i in range(len(line_cols) - 1):
        cols.append(img[0:img.shape[0], line_cols[i]:line_cols[i + 1]])
        # file_name = f"col_{i}.jpg"
        # cv2.imwrite(f'{file_name}',cols[i])
    return cols

def separate_lines(img):
    counter = 0
    averages = np.empty(img.shape[0])
    rows = np.array(range(1, img.shape[0] + 1))
    # img = ocr.binary_img(img)
    for row in img:
        averages[counter] = np.average(row)
        counter += 1

    averages = savgol_filter(averages, 41, 5)
    derivatives = calc_derivatives(averages)
    line_rows = [0]
    for i in range(0, len(derivatives) - 1):
        if derivatives[i] > 0 and derivatives[i + 1] < 0:
            if i - line_rows[-1] > 0.01 * img.shape[0]:
                line_rows.append(i)

    # for i in line_rows:
    #      for j in range(0,img.shape[1]):
    #         img[i,j] = 255
    line_rows.append(img.shape[0] - 1)
    lines = []
    # os.chdir(r'C:\Users\Jenny\Desktop\CroppedLines')
    for i in range(0, len(line_rows) - 1):
        if(line_rows[i]-10 >= 0 and line_rows[i]+10<=img.shape[0]):
            lines.append(img[line_rows[i]:line_rows[i + 1], 0:img.shape[1]])
        # file_name = f"line_{i}.jpg"
        # cv2.imwrite(f'{file_name}',lines[i])
    return lines

def separate_words(img):
    counter = 0
    standard_devs = np.empty(img.shape[1])
    img = img.transpose()
    for col in img:
        standard_devs[counter] = np.std(col)
        counter += 1

    img = img.transpose()
    standard_devs = savgol_filter(standard_devs, 41, 5)
    derivatives = calc_derivatives(standard_devs)
    line_cols = [0]
    counter = 0
    negative_slope_counter = 0
    positive_slope_counter = 0
    current_values = []
    while counter < len(derivatives):
        if derivatives[counter] < 0:
            negative_slope_counter += 1
            counter += 1
            current_values.append(standard_devs[counter])
        else:
            if negative_slope_counter > 0.15 * (img.shape[0] - 20):
                while derivatives[counter] > 0 and counter < len(derivatives) - 1:
                    current_values.append(standard_devs[counter])
                    positive_slope_counter += 1
                    counter += 1
                counter -= positive_slope_counter
                try:
                    if positive_slope_counter > 0.15 * (img.shape[0] - 20) and min(current_values) < 0.8 * np.average(standard_devs):
                        if (len(line_cols) == 0 or counter - line_cols[-1] > 0.02 * (img.shape[1])):
                            line_cols.append(counter)
                except:
                    print(current_values)
            negative_slope_counter = 0
            positive_slope_counter = 0
            current_values = []
            counter += 1

    line_cols.append(img.shape[1] - 1)
    os.chdir(r'C:\Users\Jenny\Desktop\Words')
    words = []
    for i in range(0, len(line_cols) - 1):
        words.append(img[0:img.shape[0], line_cols[i]:line_cols[i + 1]])
        # file_name = f"line_{i}.jpg"
        # cv2.imwrite(f'{file_name}',lines[i])
    return words

def transcribe(img,language='eng'):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    return pytesseract.image_to_string(img,lang=language,config='--psm 7')

def translate(str,src='la'):
    translator = Translator()
    translated = translator.translate(str,src=src)
    return translated.text

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images