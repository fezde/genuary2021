cp *.png output
ITERATIONS=543

plingo -i $ITERATIONS output/none.png
python3 build_md.py none $ITERATIONS
ffmpeg -r 2 -f concat -i md_none.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*4:trunc(ih/2)*4" none.mp4

plingo -i $ITERATIONS output/left.png
python3 build_md.py left $ITERATIONS
ffmpeg -r 2 -f concat -i md_left.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*4:trunc(ih/2)*4" left.mp4

plingo -i $ITERATIONS output/right.png
python3 build_md.py right $ITERATIONS
ffmpeg -r 2 -f concat -i md_right.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*4:trunc(ih/2)*4" right.mp4

plingo -i $ITERATIONS output/both.png
python3 build_md.py both $ITERATIONS
ffmpeg -r 2 -f concat -i md_both.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*4:trunc(ih/2)*4" both.mp4

rm output/*.png
mv *.mp4 ../../docs/09/
rm *.txt
