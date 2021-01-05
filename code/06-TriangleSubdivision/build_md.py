from sys import argv

input_file = argv[1]

with open(f"md_{input_file}.txt", "w") as md:
    md.write(f"file 'output/{input_file}.png'\n")
    md.write(f"duration 2\n")
    for j in range(int(argv[2])):
        md.write(f"file 'output/{input_file}.png_out_{j:03d}.png'\n")
        if j == 0:
            md.write(f"duration 2\n")
        eöif j == 1:
            md.write(f"duration 1\n")
        elif j == 2 or j == 3:
            md.write(f"duration 0.2\n")
        else:
            md.write(f"duration 0.1\n")
