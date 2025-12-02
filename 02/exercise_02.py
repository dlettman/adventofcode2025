import time
import pyperclip
from functools import cache

from helpers import helpers


def is_valid(num):
    if len(num) % 2 != 0:
       return True
    elif num[0:len(num)//2] == num[len(num)//2:]:
        return False
    return True

@cache
def is_valid2(num):
    for n in range(1, len(num)//2 + 1):
        if not len(num) % n == 0:
            continue
        elif num[0:n] * (len(num) // n) == num:
            return False
    return True

def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)[0]
    total = 0
    pi = puzzle_input.split(",")
    for r in pi:
        start, end = r.split("-")
        for n in range(int(start), int(end) + 1):
            if not is_valid(str(n)):
                total += int(n)
    return total


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)[0]
    total = 0
    pi = puzzle_input.split(",")
    for r in pi:
        start, end = r.split("-")
        for n in range(int(start), int(end) + 1):
            if not is_valid2(str(n)):
                total += int(n)
    return total


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
