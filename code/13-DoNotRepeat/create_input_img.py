import numpy as np
import cv2 as cv2

dim = 256 * 16

img = np.zeros((dim, dim, 3), np.uint8)

for red in range(256):
    for green in range(256):
        for blue in range(256):
            red_x = (red % 16) * 256
            red_y = int(red/16) * 256
            x = blue + red_x
            y = green + red_y
            img[y][x] = [red, green, blue]

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("output/13.png", img)
