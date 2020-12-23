plingo -i 121 23-input_0.png


# -r is the framerate (fps)
# -crf is the quality, lower means better quality, 15-25 is usually good
# -s is the resolution
# -pix_fmt yuv420p specifies the pixel format, change this as needed
yes | ffmpeg -r 4 -f image2 -s 533x300 -i 23-input_0.png_out_%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p 23-input_0.png_out.mp4

cp 23-input_0.png_out_120.png ../../docs/23/23-input_0.png_out.png
cp 23-input_0.png ../../docs/23/23-input_0.png_in.png
mv 23-input_0.png_out.mp4 ../../docs/23/23-input_0.png_out.mp4
rm 23-input_0.png_out_*.png


plingo -i 121 23-input_1.png


# -r is the framerate (fps)
# -crf is the quality, lower means better quality, 15-25 is usually good
# -s is the resolution
# -pix_fmt yuv420p specifies the pixel format, change this as needed
yes | ffmpeg -r 4 -f image2 -s 533x300 -i 23-input_1.png_out_%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p 23-input_1.png_out.mp4

cp 23-input_1.png_out_120.png ../../docs/23/23-input_1.png_out.png
cp 23-input_1.png ../../docs/23/23-input_1.png_in.png
mv 23-input_1.png_out.mp4 ../../docs/23/23-input_1.png_out.mp4
rm 23-input_1.png_out_*.png


