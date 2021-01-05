# rm *.txt
ITERATIONS=121

convert 06.jpg -resize 800x\> output/06.png
plingo -i $ITERATIONS output/06.png
# python3 build_md.py 06 $ITERATIONS
yes | ffmpeg -f concat -i md_06.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/06/06.mp4

# rm output/*.png
