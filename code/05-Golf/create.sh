echo Running plingo
plingo -i 1000 05-golf.png

echo Creating gif
convert -loop 0 -delay 200 05-golf.png -delay 25 05-golf.png_out_*.png 05-golf.gif

echo Creating mp4
yes | ffmpeg -i 05-golf.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*240:trunc(ih/2)*240" -sws_flags neighbor 05-golf.mp4
cp 05-golf.mp4 ../../docs/05/05-golf.mp4

echo Cleaning up
rm 05-golf.png_out_*.png

