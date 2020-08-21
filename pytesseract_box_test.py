import pytesseract
from pytesseract import Output
import cv2
import os
img = cv2.imread('Images/rotatednonbinary.tif')

d = pytesseract.image_to_data(img, output_type=Output.DICT,lang='lat')
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(r'C:\Users\Jenny\Desktop')
cv2.imwrite(r"pytesserat-boxes.jpg",img)