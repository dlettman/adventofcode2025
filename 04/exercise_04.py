import time

import pyperclip

from helpers import helpers

def get_grid(puzzle_input):
    paper = set()
    for y, row in enumerate(puzzle_input):
        for x, char in enumerate(row):
            if  char == "@":
                paper.add((x, y))
    return paper


def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    paper = get_grid(puzzle_input)
    total_accessible = 0
    for y, row in enumerate(puzzle_input):
        for x, char in enumerate(row):
            paper_pals = 0
            if (x, y) in paper:
                for neighbor in helpers.NEIGHBORS:
                    neighbor_coord = (x + neighbor[0], y + neighbor[1])
                    if  neighbor_coord in paper:
                        paper_pals += 1
                if paper_pals < 4:
                    total_accessible += 1
    return total_accessible


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    paper = get_grid(puzzle_input)
    moved_some = True
    total_removed = 0
    while moved_some:
        moved_some = False
        new_set = set()
        for y, row in enumerate(puzzle_input):
            for x, char in enumerate(row):
                paper_pals = 0
                if (x, y) in paper:
                    for neighbor in helpers.NEIGHBORS:
                        neighbor_coord = (x + neighbor[0], y + neighbor[1])
                        if neighbor_coord in paper:
                            paper_pals += 1
                    if paper_pals < 4:
                        total_removed += 1
                        moved_some = True
                    else:
                        new_set.add((x, y))
        paper = new_set
    return total_removed


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
