'''
 opencv practice

'''

import cv2

img = cv2.imread('9958E83F5A6C4B6D30.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # esc key
    cv2.destroyAllWindow()
elif k == ord('s'): # 's' key
    cv2.imwrite('yejingray.png',img)
    cv2.destroyAllWindow()
