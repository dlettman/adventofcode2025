import time

import pyperclip

from helpers import helpers

def parse_input(puzzle_input):
    start = None
    splitters = set()
    for y, row in enumerate(puzzle_input):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == '^':
                splitters.add((x, y))
    return start, splitters


def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    start, splitters = parse_input(puzzle_input)
    splits = 0
    beams = [start]
    current_row = start[1]
    while current_row <= len(puzzle_input):
        new_beams = []
        for beam in beams:
            if (beam[0],beam[1] + 1) in splitters:
                splits += 1
                new_beams.append((beam[0] -1, beam[1] + 1))
                new_beams.append((beam[0] +1, beam[1] + 1))
            else:
                new_beams.append((beam[0], beam[1] + 1))
        new_beams = list(set(new_beams)) # dedupe
        beams = new_beams
        current_row += 1
    return splits


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    start, splitters = parse_input(puzzle_input)
    beams = [start]
    ways_to_get_here = {(start[0], start[1]): 1}
    current_row = start[1]
    while current_row <= len(puzzle_input):
        new_beams = []
        for beam in beams:
            if (beam[0],beam[1] + 1) in splitters:
                coords = [(beam[0] -1, beam[1] + 1), (beam[0] +1, beam[1] + 1)]
            else:
                coords = [(beam[0], beam[1] + 1)]
            for coord in coords:
                new_beams.append(coord)
                if coord in ways_to_get_here:
                    ways_to_get_here[coord] += ways_to_get_here[(beam[0], beam[1])]
                else:
                    ways_to_get_here[coord] = ways_to_get_here[(beam[0], beam[1])]
        beams = list(set(new_beams)) # dedupe
        current_row += 1
    timelines = 0
    for loc, count in ways_to_get_here.items():
        if loc[1] == len(puzzle_input) - 1:
            timelines += count
    return timelines


if __name__ == "__main__":
    print("*** PART ONE ***\n")
    print(f"Test result = {part_one('inputtest.txt')}\n")
    onestart = time.time()
    p1result = part_one("input.txt")
    oneend = time.time()
    print(f"REAL RESULT = {p1result}")
    print(f"Time = {oneend - onestart}")
    print("\n")
    print("*** PART TWO ***\n")
    print(f"Test result = {part_two('inputtest.txt')}\n")
    twostart = time.time()
    p2result = part_two("input.txt")
    twoend = time.time()
    print(f"REAL RESULT = {p2result}")
    print(f"Time = {twoend - twostart}")
    if p1result:
        pyperclip.copy(p1result)
    elif p2result:
        pyperclip.copy(p2result)
