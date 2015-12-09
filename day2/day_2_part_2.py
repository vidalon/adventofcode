import sys

feet_of_paper_needed = 0

input = []

with open("./day_2_part_2.input") as f:
    input = f.readlines()

for measure in input:
    length, height, width = measure.split("x")

    length = int(length)
    height = int(height)
    width = int(width)

    combinations = [length, height, width]

    biggest_dimension = 0
    ribbon_length = 0

    for c in combinations:
        if c > biggest_dimension:
            biggest_dimension = c
        ribbon_length += c*2

    #Substract the biggest side, we don't need that one
    ribbon_length -= biggest_dimension*2

    feet_of_paper_needed += ribbon_length + (length*height*width)

print feet_of_paper_needed