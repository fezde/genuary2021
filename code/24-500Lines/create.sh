#plingo -i 121 500lines.png

ffmpeg -r 2 -f concat -i moviedescription.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" 24.mp4

rm *_out_???.png
mv 24.mp4 ../../docs/24/