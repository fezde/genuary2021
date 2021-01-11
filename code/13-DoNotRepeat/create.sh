render() {
    plingo -i $ITERATIONS output/$FILE.png
    python3 build_md.py $FILE $ITERATIONS
    yes | ffmpeg -f concat -i md_$FILE.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/13/$FILE.mp4
}

#######################################################################
# Main
#######################################################################

ITERATIONS=121
FILE=13

rm *.txt
python3 create_input_img.py

render

# rm output/*.png
