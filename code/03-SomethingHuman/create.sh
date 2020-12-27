echo Initializing

rm used_concepts.json
rm output/table.html

convert initial.jpg -resize x600\> output/000.png
plingo output/000.png


for i in $(seq 0 120); do
    python3 step.py $i
done

mv output/*.png ../../docs/03/
mv output/table.html .

sed '/<!--replaceme-->/{
    s/<!--replaceme-->//g
    r table.html
}' template.html > ../../docs/03/index.html

rn table.html
rm temp.jpg

