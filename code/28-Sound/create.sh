yes | ffmpeg -i test2.m4a input.wav
python3 snd2img.py input.wav output/temp
plingo  output/temp.png
python3 img2snd.py output/temp.png
python3 img2snd.py output/temp.png_out.png

mv output/temp.png ../../docs/28/before.png
mv output/temp.png_out.png ../../docs/28/after.png
yes | ffmpeg -i output/temp.png.wav ../../docs/28/before.mp3
yes | ffmpeg -i output/temp.png_out.png.wav ../../docs/28/after.mp3
yes | ffmpeg -i input.wav ../../docs/28/orig.mp3
rm output/*.wav
