# keep a list of unique spots each line crosses
# then find the intersection (where the lines meet)
# and find the one closest to the central port

def move(location, segment, spots, steps_taken):
    distance = int(segment[1:])
    starting_steps = steps_taken[location]

    if segment[0] == 'L':
        new_location = location[0] - distance, location[1]
        for x in range(new_location[0], location[0]+1):
            new_spot = (x, location[1])
            if new_spot not in spots:
                spots.add(new_spot)
                steps_taken[new_spot] = starting_steps + (location[0] - x)
    elif segment[0] == 'R':
        new_location = location[0] + distance, location[1]
        for index, x in enumerate(range(location[0], new_location[0]+1)):
            new_spot = (x, location[1])
            if new_spot not in spots:
                spots.add(new_spot)
                steps_taken[new_spot] = starting_steps + index
    elif segment[0] == 'D':
        new_location = location[0], location[1] - distance
        for y in range(new_location[1], location[1]+1):
            new_spot = (location[0], y)
            if new_spot not in spots:
                spots.add(new_spot)
                steps_taken[new_spot] = starting_steps + (location[1] - y)
    elif segment[0] == 'U':
        new_location = location[0], location[1] + distance
        for index, y in enumerate(range(location[1], new_location[1]+1)):
            new_spot = (location[0], y)
            if new_spot not in spots:
                spots.add(new_spot)
                steps_taken[new_spot] = starting_steps + index
    else:
        assert True == False
    
    return new_location

def get_spots_from_path(path):
    spots = set()
    location = 0,0
    steps_taken = {location: 0}

    for segment in path:
        location = move(location, segment, spots, steps_taken)

    return spots, steps_taken

with open("input.txt") as f:
    lines = f.readlines()
    path1 = lines[0].strip().split(',')
    path2 = lines[1].strip().split(',')

# should be 610 for part 2
# path1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
# path2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')

# should be 410 for part 2
# path1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
# path2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')

# should be 30 for part 2
# path1 = "R8,U5,L5,D3".split(',')
# path2 = "U7,R6,D4,L4".split(',')

spots1, steps_taken1 = get_spots_from_path(path1)
spots2, steps_taken2 = get_spots_from_path(path2)

common_spots = spots1.intersection(spots2)
common_spots.remove((0,0))
print(f"{len(common_spots)} intersection points.")

min_distance = min((abs(x) + abs(y) for x,y in common_spots))
print(f"Part 1: {min_distance}")

min_steps = min((steps_taken1[spot] + steps_taken2[spot] for spot in common_spots))
print(f"Part 2: {min_steps}")
