import cv2

img = cv2.imread("Mona_Lisa.jpg" ,0)

invert = cv2.bitwise_not(img)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(img , invertedblur , scale=256.0)

cv2.imshow("Black pen" , sketch)
cv2.imwrite("sketch.png" , sketch)
cv2.waitKey()