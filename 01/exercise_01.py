import time

import pyperclip

from helpers import helpers

def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    output = 0
    curr = 50
    for line in puzzle_input:
        lr = line[0]
        num = int(line[1:])
        if lr == "L":
            curr = (curr - num) % 100
        elif lr == "R":
            curr = (curr + num) % 100
        if curr == 0:
            output += 1
    return output


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    output = 0
    curr = 50
    for line in puzzle_input:
        lr = line[0]
        num = int(line[1:])
        if lr == "L":
            rot, curr = divmod(curr - num, 100)
            output += abs(rot)
        elif lr == "R":
            if curr == 0:
                output += 1
            rot, curr = divmod(num + curr, 100)
            output += abs(rot)
            if curr == 0: # don't double-count!
                output -= 1
    if curr == 0: # it won't be, but still...
        output += 1
    return output


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
