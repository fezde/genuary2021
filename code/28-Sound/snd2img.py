import scipy.io.wavfile as wav
import numpy as np
from math import floor, sqrt
import cv2 as cv2
from sys import argv

# from scipy import signal

input_data = wav.read(argv[1])

samplerate = input_data[0]
audio_data = input_data[1].astype('float64')
print(samplerate)
print(np.max(audio_data))
print(np.min(audio_data))

# Normalize (we need it for RGB)
minimum = np.min(audio_data)
if minimum < 0:
    minimum *= -1
maximum = np.max(audio_data)
span = minimum + maximum
audio_data += minimum
audio_data /= span
audio_data *= 256

width = int(floor(sqrt(audio_data.shape[0])))
height = int(audio_data.shape[0] / width)

print(width)
print(height)

output_img = np.zeros((height, width, 3), dtype="uint8")
for x in range(width):
    for y in range(height):
        pos = x*height + y
        output_img[y][x][0] = audio_data[pos][0]
        output_img[y][x][1] = audio_data[pos][1]
        output_img[y][x][2] = (audio_data[pos][0] + audio_data[pos][1]) / 2


print(output_img.shape)
output_img = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)
cv2.imwrite(f"{argv[2]}.png", output_img)
