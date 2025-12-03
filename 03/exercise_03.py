import time

import pyperclip

from helpers import helpers


def get_joltage(line, num_batteries=12):
    last_idx = 0
    num_so_far = ""
    for n in range(num_batteries):
        best_so_far, best_idx = 0, 0
        for idx, char in enumerate(line[last_idx:((len(line) + 1)- (num_batteries-n))]):
            if int(char) > best_so_far:
                best_so_far = int(char)
                best_idx = idx
        last_idx = best_idx + last_idx + 1
        num_so_far += str(best_so_far)
    return int(num_so_far)

def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    return sum([get_joltage(line, num_batteries=2) for line in puzzle_input])


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    return sum([get_joltage(line) for line in puzzle_input])


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
