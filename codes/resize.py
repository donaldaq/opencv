#image resize

import cv2
import numpy as np

img = cv2.imread('9958E83F5A6C4B6D30.jpg')

# 행 : Height, 열:width
height, width = img.shape[:2]

# 이미지 축소
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 이미지 축소 4분의 1
shrink2 = cv2.resize(img, None, fx=0.125, fy=0.125, interpolation=cv2.INTER_AREA)

# Manual Size지정
zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

# 배수 Size지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)


cv2.imshow('Original', img)
cv2.imshow('Shrink / 2', shrink)
cv2.imshow('Shrink / 4', shrink2)
#cv2.imshow('Zoom1', zoom1)
#cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()