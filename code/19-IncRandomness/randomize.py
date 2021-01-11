from random import randint

input_str = "#genuary2021"
input_list = [char for char in input_str]

print(input_str)

for _ in range(13):
    i1 = i2 = randint(0, len(input_str)-1)

    while i1 == i2:
        i2 = randint(0, len(input_str)-1)

    # print(i1)
    # print(i2)
    input_list[i1], input_list[i2] = input_list[i2], input_list[i1]

    print("".join(input_list))
