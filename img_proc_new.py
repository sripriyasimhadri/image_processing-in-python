# -*- coding: utf-8 -*-
"""
Created on Thu May 31 13:43:27 2018

@author: sripriya
"""
# import the necessary packages
import pytesseract
from PIL import Image
# load the image 
img=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\image1.png')
#extract text from image
result=pytesseract.image_to_string(img)
#print text
print(result)