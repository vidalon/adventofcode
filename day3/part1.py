from collections import defaultdict

visited_houses = defaultdict(int)
santas_position = [0,0]
input = None

with open("./part1.input") as f:
    input = f.read()

visited_houses[str(santas_position)] = 1

for c in input:
    if c == '^':
        #move one up on the Y axis
        santas_position[1] += 1
    elif c == 'v':
        #move one up on the Y axis
        santas_position[1] -= 1
    elif c == '<':
        #move one left on the X axis
        santas_position[0] -= 1
    elif c == '>':
        #move one right on the X axis
        santas_position[0] += 1

    visited_houses[str(santas_position)] += 1

print len(visited_houses.keys())
