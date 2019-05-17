# -*- coding: utf-8 -*-
"""
Created on Tue May 29 09:35:30 2018

@author: sripriya
"""
# import the necessary packages
import pytesseract
from PIL import Image
import cv2
import numpy as np
# load the image 
img=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\images.jpg')
#print the type of image
print(type(img))
#convert the image type into numpy array for processing
image_data = np.asarray(img)
#print type of image_data object
print(type(image_data))
#denoising the image
dst = cv2.fastNlMeansDenoisingColored(image_data,None,10,10,7,21)
#saving the denoised image
cv2.imwrite(r'C:\Users\sripriya\Desktop\image_processing\images\deionise.png', dst)
#to convert tesseract_cmd file to tesseract.exe
#pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract 4.0.0/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
#converting the image into grayscale
gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
#saving the grayscale image
cv2.imwrite(r'C:\Users\sripriya\Desktop\image_processing\images\enhancedGrayscaleLineCapture.png', gray)
#to increase the threshold of the image
th1 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                            cv2.THRESH_BINARY,11,2)
ret2,th2 = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blue, green, red = cv2.split(image_data)
blue_edges = cv2.Canny(blue, 100, 10)       
green_edges = cv2.Canny(green, 100, 10)
red_edges = cv2.Canny(red, 100, 10)
edges = blue_edges | green_edges | red_edges
#saving enhanced gray scale threshold,grayscaled images
cv2.imwrite(r'C:\Users\sripriya\Desktop\image_processing\images\enhancedGrayscaleThresholdLineCapture.png', th2)
cv2.imwrite(r'C:\Users\sripriya\Desktop\image_processing\images\bluegreenred.png', edges)
img2=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\enhancedGrayscaleThresholdLineCapture.png')
img1=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\bluegreenred.png')
images=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\deionise.png')
#extract text from denoised image
result=pytesseract.image_to_string(images)
#print text
print(result)
#storing the text in destined document
with open('C:\Users\sripriya\Desktop\image_processing\magic.txt',mode='w') as file:
    file.write(result.encode('utf-8')) 
    