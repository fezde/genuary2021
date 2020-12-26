cp input.png output/02.png
cd output
plingo -i 121 02.png
cd ..

yes | ffmpeg -r 2 -f concat -i moviedescription.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" 02.mp4
mv 02.mp4 ../../docs/02
rm output/02*