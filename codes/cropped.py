import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('9958E83F5A6C4B6D30.jpg', 0)

print(img.shape)

x, y = img.shape

print(x)
print(y)

_x = 64
_y = 64
k = 0

# 이미지 하나씩 자르기
for i in range(0, y, _y):
    for j in range(0, x, _x):
        k = k + 1
        if k == 5:
            testimg = img[i:i+_x, j:j+_y]
            cv2.imshow('testimage',testimg)




cv2.imshow('image',img)
cv2.waitKey(0)