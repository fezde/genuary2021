import os

# Create move descriptions
for i in range(1, 7):
    with open(f"md_0{(i)}.txt", "w+") as fh:
        fh.write(f"file '07_0{i}.png'\n")
        fh.write("duration 1\n")
        fh.write("\n")
        for j in range(121):
            fh.write(f"file 'output_0{i}/07_0{i}.png_out_{j:03d}.png'\n")
            fh.write("duration 0.333333\n")

    os.system(f"cp 07_0{i}.png output_0{i}/")
    os.system(f"plingo -i 121 output_0{i}/07_0{i}.png")
    os.system(
        f'ffmpeg -r 2 -f concat -i md_0{(i)}.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" 07_0{i}.mp4')
    os.system(f"rm output_0{i}/*")
