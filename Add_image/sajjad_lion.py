import cv2
import numpy as numPy

img1 = cv2.imread('sajjad (2).jpg',0)
img2 = cv2.imread('lion.jpg',0)

img1 = cv2.resize(img1,(150,250))
img2 = cv2.resize(img2,(150,250))


result1 = img1//2 + img2//8
result2 = img1//2 + img2//4
result3 = img1//2 + img2//2
result4 = img1//4 + img2//2


Result = numPy.concatenate((result1,result2,result3,result4),axis=1)

cv2.imshow('sajjad_lion',Result)
cv2.imwrite("sajad_lion.jpg", Result)
cv2.waitKey()