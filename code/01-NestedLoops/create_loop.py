import cv2 as cv2
import numpy as np

steps = 121
img = cv2.imread("loop.png")

angle = 360.0 / steps
image_center = tuple(np.array(img.shape[1::-1]) / 2)

for i in range(steps):
    rot_mat = cv2.getRotationMatrix2D(image_center, -i*angle, 1.0)
    new = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    cv2.imwrite(f"output/loop_{i:03d}.png", new)
