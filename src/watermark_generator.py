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

random.seed(a=KEY)
random_points = random.sample(range(IMG_SIZE), WATERMARK_SIZE)

owner_img = cv2.imread('images\owner_img.jpg', 0)

for k in range(0, 7):
    master_img = cv2.imread('images\master_images\master_img_'+str(k)+'.jpg', 0)
    watermark_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)

    i = 0
    j = 0

    for i in range(0, WATERMARK_HEIGHT):
        for j in range(0, WATERMARK_WIDTH):
            watermark_img[i, j] = xor(master_img[i, j], owner_img[i, j])

    watermark_img = (255-watermark_img)
    kernel = np.ones((4,4),np.uint8)
    watermark_img = cv2.medianBlur(watermark_img, 3)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_OPEN, kernel)
    watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_CLOSE, kernel)
    watermark_img = (255-watermark_img)

    cv2.imwrite('images\\regenerated_watermarks\\watermark_img_'+str(k)+'.jpg', watermark_img)
    print(k)
print("Done")