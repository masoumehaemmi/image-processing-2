from random import randint
import cv2

img = cv2.imread('chess_pieces.jpg', 0)
rows, cols = img.shape

for i in range(rows):
    for j in range(cols):
        rand_num = randint(0, 200)
        if rand_num < 10:
            img[i, j] = 255 - img[i, j]

cv2.imwrite('chess_noise.jpg', img)
cv2.imshow('chess_noise', img)
cv2.waitKey()