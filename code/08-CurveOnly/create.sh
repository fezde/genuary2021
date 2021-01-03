rm *.txt
ITERATIONS=543

convert 08.jpg -resize 800x\> output/08.png
plingo -i $ITERATIONS output/08.png
python3 build_md.py 08 $ITERATIONS
yes | ffmpeg -r 2 -f concat -i md_08.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/08/08.mp4
rm output/*.png
