convert input.jpg -resize 1200x\> output/step_0.png
plingo output/step_0.png

END=10

for i in $(seq 1 $END); do
    echo $i
    python3 do_subdiv.py $i
    plingo output/step_$i.png
done

mv output/*.png ../../docs/14/assets/
