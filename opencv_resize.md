## Transformations

변환이란 수학적으로 표현하면 아래와 같습니다.

> - 좌표 x를 좌표 x’로 변환하는 함수

예로는 사이즈 변경(Scaling), 위치변경(Translation), 회전(Rotaion) 등이 있습니다. 변환의 종류에는 몇가지 분류가 있습니다.

> - 강체변환(Ridid-Body) : 크기 및 각도가 보존(ex; Translation, Rotation)
> - 유사변환(Similarity) : 크기는 변하고 각도는 보존(ex; Scaling)
> - 선형변환(Linear) : Vector 공간에서의 이동. 이동변환은 제외.
> - Affine : 선형변환과 이동변환까지 포함. 선의 수평성은 유지.(ex;사각형->평행사변형)
> - Perspective : Affine변환에 수평성도 유지되지 않음. 원근변환



### Scaling

Scaling은 이미지의 사이즈가 변하는 것 입니다. OpenCV에서는 `cv2.resize()` 함수를 사용하여 적용할 수 있습니다. 사이즈가 변하면 pixel사이의 값을 결정을 해야 하는데, 이때 사용하는 것을 보간법(Interpolation method)입니다. 많이 사용되는 보간법은 사이즈를 줄일 때는 `cv2.INTER_AREA` , 사이즈를 크게할 때는 `cv2.INTER_CUBIC` , `cv2.INTER_LINEAR` 을 사용합니다.





cv2.resize(*img*, *dsize*, *fx*, *fy*, *interpolation*)

**Parameters** 

- img - Image
- dsize - Manual Size. 가로, 세로 형태의 tuple(ex; (100,200))
- fx - 가로 사이즈의 배수. 2배로 크게 하려면 1/2로 줄이려면 0.5
- fy - 세로 사이즈의 배수
- interpolation - 보간법 

```python
#-*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('images/logo.png')

# 행 : Height, 열:width
height, width = img.shape[:2]

# 이미지 축소
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Manual Size지정
zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

# 배수 Size지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)


cv2.imshow('Origianl', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```



1. Original Image

![original](https://user-images.githubusercontent.com/26396102/60477620-bbcaf000-9cba-11e9-9c7d-506044e19972.PNG)



2. 1/2 Image

![2분의1 image](https://user-images.githubusercontent.com/26396102/60477678-dbfaaf00-9cba-11e9-8ad0-49966f0ffc83.PNG)

3. 1/4 image

![4분의 1 image](https://user-images.githubusercontent.com/26396102/60477718-0d737a80-9cbb-11e9-9acd-0f210c7f4eb0.PNG)











