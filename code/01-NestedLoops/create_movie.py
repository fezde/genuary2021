import cv2 as cv2
from math import floor


first_image = cv2.imread("loop.png")
frames_per_second = 10
fourcc = cv2.VideoWriter_fourcc(*'MP4V')

video_name = "loop.mp4"
out = cv2.VideoWriter(video_name, fourcc, frames_per_second, (first_image.shape[1], first_image.shape[0]))

for _ in range(10):
    out.write(first_image)

magic_number = 121
multiplier = 8

for i in range(multiplier * magic_number):
    x = int(i % (2*magic_number))
    if x >= magic_number:
        x = magic_number - (x-magic_number)
    y = floor(i/multiplier)

    file_name = f"output/loop_{y:03d}.png_out_{x:03d}.png"
    print(file_name)
    out.write(cv2.imread(file_name))
    if x < 10:
        for _ in range(3):
            out.write(cv2.imread(file_name))

out.release()

for at in [0, 1, 2,  30, 60, 90, 120]:
    video_name = f"loop_at_{(at+1):03d}.mp4"
    out = cv2.VideoWriter(video_name, fourcc, frames_per_second, (first_image.shape[1], first_image.shape[0]))
    for i in range(magic_number):
        file_name = f"output/loop_{i:03d}.png_out_{at:03d}.png"
        out.write(cv2.imread(file_name))
    out.release()

video_name = f"loop_at_000.mp4"
out = cv2.VideoWriter(video_name, fourcc, frames_per_second, (first_image.shape[1], first_image.shape[0]))
for i in range(magic_number):
    file_name = f"output/loop_{i:03d}.png"
    out.write(cv2.imread(file_name))
out.release()
