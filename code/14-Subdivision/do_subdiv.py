import cv2 as cv2
import numpy as np
from sys import argv

input_count = int(argv[1])

file_name = f"output/step_{input_count-1}.png_out.png"
print(f"Subdiving {file_name}")
input_img = cv2.imread(file_name)
input_img = cv2.resize(input_img, (400, 400))

orig_img = cv2.imread("output/step_0.png")
orig_img = cv2.resize(orig_img, (400, 400))

l_img = np.zeros((1200, 1200, 3), np.uint8)

x_offset = y_offset = 50
#l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

# y_offset = 400
# x_offset = 400
# l_img[y_offset:y_offset+orig_img.shape[0], x_offset:x_offset+orig_img.shape[1]] = orig_img

y_offset = 0
x_offset = 0
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img
x_offset = 400
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img
x_offset = 800
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img

y_offset = 400
x_offset = 0
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img
x_offset = 800
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img

y_offset = 800
x_offset = 0
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img
x_offset = 400
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img
x_offset = 800
l_img[y_offset:y_offset+input_img.shape[0], x_offset:x_offset+input_img.shape[1]] = input_img

cv2.imwrite(f"output/step_{input_count}.png", l_img)
