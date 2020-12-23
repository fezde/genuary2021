# rotate the loop image
python3 create_loop.py

# create the plingo outputs
for INPUT in output/loop_???.png; do
    plingo -i 121 $INPUT
done

# create the videos iterating over the "double loop" created above
python3 create_movie.py

