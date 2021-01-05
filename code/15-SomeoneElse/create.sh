rm *.txt
ITERATIONS=121

convert InputAmelie.jpeg -resize 800x\> output/15.png
plingo -i $ITERATIONS output/15.png
python3 build_md.py 15 $ITERATIONS
yes | ffmpeg -f concat -i md_15.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/15/15.mp4

rm output/*.png
