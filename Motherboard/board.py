import cv2

img1 = cv2.imread("board - origin.bmp", 0)
img2 = cv2.imread("board - test.bmp", 0)
img2 = img2[:, ::-1]

result = cv2.subtract(img1, img2)
rows, cols = result.shape
result2 = cv2.absdiff(img1, img2)

for i in range(rows):
    for j in range(cols):
        if result[i][j] > 0:
            result[i][j] = 255

cv2.imwrite("board.jpg", result2)
cv2.imwrite("board.jpg", result)
cv2.imshow("board", result)
cv2.waitKey()