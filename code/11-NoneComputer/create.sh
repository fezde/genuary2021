render() {
    convert $FILE.jpg -resize 800x\> output/$FILE.png
    plingo -i $ITERATIONS output/$FILE.png
    python3 build_md.py $FILE $ITERATIONS
    yes | ffmpeg -f concat -i md_$FILE.txt -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ../../docs/11/$FILE.mp4
}

#######################################################################
# Main
#######################################################################

ITERATIONS=121

rm *.txt

for FILE in "11-bw" "11-col"; do
    echo $FILE
    render
done

rm output/*.png
