import sys

feet_of_paper_needed = 0

input = []

with open("./part1.input") as f:
    input = f.readlines()

for measure in input:
    length, height, width = measure.split("x")

    length = int(length)
    height = int(height)
    width = int(width)

    combinations = [length * height, length * width, height * width]

    lowest_combination = sys.maxint

    for c in combinations:
        if c < lowest_combination:
            lowest_combination = c
        feet_of_paper_needed += c*2

    feet_of_paper_needed += lowest_combination

print feet_of_paper_needed