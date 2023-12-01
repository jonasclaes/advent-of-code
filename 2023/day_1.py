import re
from aocd import submit
from aocd.models import Puzzle

YEAR = 2023
DAY = 1

puzzle = Puzzle(year=YEAR, day=DAY)


def part_one(input_data: str):
    input_data = input_data.splitlines()

    answer = 0

    for line in input_data:
        words = re.findall("(\\d)", line)
        answer += int("".join([d for d in [words[0], words[-1]]]))

    submit(answer, part="a", year=YEAR, day=DAY)


def part_two(input_data: str):
    input_data = input_data.splitlines()

    answer = 0

    text_to_digit_mappings = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    for line in input_data:
        words = re.findall(
            "(?=(" + "|".join(text_to_digit_mappings.keys()) + "|\\d))", line)

        answer += int("".join([d if d.isdigit() else text_to_digit_mappings[d]
                               for d in [words[0], words[-1]]]))

    submit(answer, part="b", year=YEAR, day=DAY)


part_one(puzzle.input_data)
part_two(puzzle.input_data)
