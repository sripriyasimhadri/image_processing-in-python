#-*- coding: utf-8 -*-
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
image=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\text.png')
#convert the image type into numpy array for processing
img= np.asarray(image)
#converting the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)
#to increase the threshold of the image
thresh = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
coords = np.column_stack(np.where(thresh > 0))
#getting angle of text in image
angle = cv2.minAreaRect(coords)[-1]
# the cv2.minAreaRect function returns values in the
# range [-90, 0); as the rectangle rotates clockwise the
# returned angle trends to 0 -- in this special case we
# need to add 90 degrees to the angle
if angle < -45:
	angle = -(90+angle)
# otherwise, just take the inverse of the angle to make
# it positive
else:
	angle = -angle
50
# rotate the image to deskew it
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(img, M, (w, h),
	flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
# draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
	(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) 
# show the output image and text
print("[INFO] angle: {:.3f}".format(angle))
cv2.imwrite(r'C:\Users\sripriya\Desktop\image_processing\images\rot.png',rotated)
images=Image.open(r'C:\Users\sripriya\Desktop\image_processing\images\rot.png')
text = pytesseract.image_to_string(images,lang='eng')
print(text)
