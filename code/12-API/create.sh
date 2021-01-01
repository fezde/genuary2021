# rm *_out_*.png
# rm *_out_*.png.txt

# plingo -i 10 12.png

for filename in *.png; do
    echo Analyzing $filename
    python3 analyze.py $filename > "$filename.txt"
done