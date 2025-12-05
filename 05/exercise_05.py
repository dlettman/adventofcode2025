import time

import pyperclip

from helpers import helpers

def parse_input(puzzle_input):
    ranges, ids = puzzle_input.split('\n\n')
    ranges = ranges.split('\n')
    parsed_ranges = [[int(item) for item in range.split("-")] for range in ranges]
    ids = ids.split('\n')
    return parsed_ranges, ids

def is_fresh(id, ranges):
    for range in ranges:
        if int(range[0]) <= int(id) <= int(range[1]):
            return True
    return False


def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename, split=False)
    ranges, ids = parse_input(puzzle_input)
    total = sum([1 for id in ids if is_fresh(id, ranges)])
    return total


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename, split=False)
    ranges, _ = parse_input(puzzle_input)
    made_a_change = True
    while made_a_change:
        made_a_change = False
        ranges = sorted(ranges, key=lambda x: int(x[0]))
        for idx, range in enumerate(ranges):
            try:
                if range[1] >= ranges[idx+1][0]:
                    if ranges[idx+1][1] > range[1]:
                        range[1] = ranges[idx+1][1]
                    ranges.pop(idx + 1)
                    made_a_change = True
                    break
            except IndexError:
                pass
    return sum([(range[1] - range[0]) + 1 for range in ranges])



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
