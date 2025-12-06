import time
from math import prod
import pyperclip

from helpers import helpers

def parse_input(puzzle_input):
    split_lines = [[int(item) if item.isdigit() else item for item in line.split()] for line in puzzle_input]
    columns = zip(*split_lines)
    return columns

def parse_input2(puzzle_input):
    last_idx = 0
    curr_idx = 0
    sub_arrays = []
    while True:
        try:
            if all ([item[curr_idx] == " " for item in puzzle_input]):
                sub_arrays.append([row[last_idx:curr_idx] for row in puzzle_input])
                last_idx = curr_idx + 1
            curr_idx += 1
        except IndexError:
            longest = max([len(item) for item in puzzle_input])
            sub_arrays.append([row[last_idx:longest] for row in puzzle_input])
            break
    return sub_arrays


def part_one(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    columns = parse_input(puzzle_input)
    total = 0
    for column in columns:
        operation = column[-1]
        if operation == '+':
            total += sum(column[0:-1])
        elif operation == '*':
            total += prod(column[0:-1])
    return total


def part_two(input_filename):
    puzzle_input = helpers.parse_input(input_filename)
    columns = parse_input2(puzzle_input)
    total = 0
    for column in columns:
        components = []
        longest = max([len(item) for item in column])
        curr = longest - 1
        while curr >= 0:
            current_component = ""
            for num in column[0:-1]:
                if len(num) >= curr + 1: # use this number
                    current_component += num[curr]
            components.append(current_component)
            curr -= 1
        operation = column[-1].strip()
        if operation == '+':
            total += sum([int(item.strip()) for item in components])
        elif operation == '*':
            total += prod([int(item.strip()) for item in components])
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
