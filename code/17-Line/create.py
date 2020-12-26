import cv2 as cv2
from math import floor
import numpy as np
from plingo import Plingo
from copy import deepcopy

color_picker = cv2.imread("felix-dubois-robert-CuEvrPd3NYc-unsplash.jpg")
color_picker = cv2.cvtColor(color_picker, cv2.COLOR_BGR2RGB)

print(color_picker.shape)
width = color_picker.shape[1]
height = 320
picking_row = 800

output = np.zeros((height, width, 3), np.uint8)
overview = np.zeros((height, width, 3), np.uint8)

lingo = Plingo()

for i in range(121):
    x = floor(i * (width/121)) + 3

    for j in range(-1, 2):
        color = color_picker[picking_row][x+j]
        print(f"{i:03d} - {x+j:04d}: {color}")
        output[:, x+j] = color
        overview[:, x+j] = color

    lingo._next_image_data = output
    lingo._height = height
    lingo._width = width
    lingo.execute(show_progressbar=True, iterations=1, save_output=False)
    output = lingo._next_image_data

    cv2.imwrite(f"output/ouput_{i:03d}.png", output)

cv2.imwrite(f"ouput_overview.png", overview)
