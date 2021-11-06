import cv2

img1 = cv2.imread("board - origin.bmp" , 0)
img2 = cv2.imread("board - test.bmp" , 0)

mask = cv2.flip(img2, 1)

new_img = cv2.subtract(img1 , mask)

result = img1 * mask


#cv2.imwrite("output.jpg" ,  result)
cv2.imshow("output" , result)
cv2.waitKey()