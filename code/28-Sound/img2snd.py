import cv2 as cv2
import numpy as np
import scipy.io.wavfile as wav
from sys import argv

data_img = cv2.imread(argv[1])
print(data_img.shape)
print(data_img.dtype)

width = data_img.shape[1]
height = data_img.shape[0]
samplerate = 48000
maximum = 972
minimum = -978
span = maximum - minimum


output_sound = np.zeros((width*height, 2), dtype="int16")

for x in range(width):
    for y in range(height):
        pos = x*height + y
        output_sound[pos][0] = ((data_img[y][x][0] / 256) + minimum) * span
        output_sound[pos][1] = ((data_img[y][x][1] / 256) + minimum) * span

wav.write(f"{argv[1]}.wav", samplerate, output_sound)
