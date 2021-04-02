import cv2
import random
import numpy as np

IMG_WIDTH = 1200
IMG_HEIGHT = 800
WATERMARK_WIDTH = 256
WATERMARK_HEIGHT = 256

IMG_SIZE = IMG_HEIGHT * IMG_WIDTH
WATERMARK_SIZE = WATERMARK_HEIGHT * WATERMARK_WIDTH

KEY = 1001
THRESH = 75

def xor(x ,y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 and y != 0:
        return 255
    elif x != 0 and y == 0:
        return 255
    elif x !=0 and y != 0:
        return 0

def mean_neighbour(img, x, y):
    val = 0
    num = 0
    i = x
    j = y
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x + 1
    j = y + 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x - 1
    j = y - 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x + 1
    j = y
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x
    j = y + 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x + 1
    j = y - 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x - 1
    j = y + 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    i = x - 1
    j = y
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val = val + img[i, j]
        num += 1
    i = x
    j = y - 1
    if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
        val += img[i, j]
        num += 1
    
    return val/float(num)

og_img = cv2.imread('images\original_image.jpg',0)
watermark_img = cv2.imread('images\watermark.jpg', 0)
ret,watermark_img = cv2.threshold(watermark_img,127,255,cv2.THRESH_BINARY)

master_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)
owner_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)

random.seed(a=KEY)
random_points = random.sample(range(IMG_SIZE), WATERMARK_SIZE)

i = 0
j = 0

for k in random_points:
    x = k // IMG_WIDTH
    y = k % IMG_WIDTH
    if mean_neighbour(og_img, x, y) > THRESH:
        master_img[i,j] = 255
    j += 1
    if j == 256:
        j = 0
        i += 1

for i in range(0, WATERMARK_HEIGHT):
    for j in range(0, WATERMARK_WIDTH):
        owner_img[i, j] = xor(master_img[i, j], watermark_img[i, j])

cv2.imshow('M', master_img)
cv2.imshow('O', owner_img)
cv2.imwrite('images\master_img.jpg', master_img)
cv2.imwrite('images\owner_img.jpg', owner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()