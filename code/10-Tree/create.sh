rm *.txt
ITERATIONS=121

convert tree1.jpg -resize 800x\> output/tree1.png
plingo -i $ITERATIONS output/tree1.png
python3 build_md.py tree1 $ITERATIONS
yes | ffmpeg -r 2 -f concat -i md_tree1.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/10/tree1.mp4

convert tree2.jpg -resize 800x\> output/tree2.png
plingo -i $ITERATIONS output/tree2.png
python3 build_md.py tree2 $ITERATIONS
yes | ffmpeg -f concat -i md_tree2.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/10/tree2.mp4

convert tree3.jpg -resize x800\> output/tree3.png
plingo -i $ITERATIONS output/tree3.png
python3 build_md.py tree3 $ITERATIONS
yes | ffmpeg -f concat -i md_tree3.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/10/tree3.mp4

convert tree4.jpg -resize x800\> output/tree4.png
plingo -i $ITERATIONS output/tree4.png
python3 build_md.py tree4 $ITERATIONS
yes | ffmpeg -f concat -i md_tree4.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/10/tree4.mp4

rm output/*.png
