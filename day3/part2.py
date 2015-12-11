from collections import defaultdict

visited_houses = defaultdict(int)
is_it_santas_turn = True
santas_position = [0,0]
robots_position = [0,0]
input = None

with open("./part2.input") as f:
    input = f.read()

visited_houses[str(santas_position)] = 1
visited_houses[str(robots_position)] += 1

for c in input:
    if c == '^':
        #move one up on the Y axis
        if is_it_santas_turn:
            santas_position[1] += 1
        else:
            robots_position[1] += 1
    elif c == 'v':
        #move one up on the Y axis
        if is_it_santas_turn:
            santas_position[1] -= 1
        else:
            robots_position[1] -= 1
    elif c == '<':
        #move one left on the X axis
        if is_it_santas_turn:
            santas_position[0] -= 1
        else:
            robots_position[0] -= 1
    elif c == '>':
        #move one right on the X axis
        if is_it_santas_turn:
            santas_position[0] += 1
        else:
            robots_position[0] += 1

    if is_it_santas_turn:
        visited_houses[str(santas_position)] += 1
    else:
        visited_houses[str(robots_position)] += 1
    is_it_santas_turn = not is_it_santas_turn

print len(visited_houses.keys())