import cv2

img1 = cv2.imread("a.tif", 0)
img2 = cv2.imread("b.tif", 0)

result = img2 - img1

cv2.imshow("pass a&b", result)
cv2.imwrite("pass a&b.jpg", result)
cv2.waitKey()