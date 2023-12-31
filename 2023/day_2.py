from functools import reduce
import re
from typing import List
from aocd import submit
from aocd.models import Puzzle

YEAR = 2023
DAY = 2

puzzle = Puzzle(year=YEAR, day=DAY)


def part_one(input_data: str):
    input_data = input_data.splitlines()

    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    valid_game_ids: List[int] = []

    for game in input_data:
        game_is_valid = True
        throws = re.findall(
            r"(Game \d+:|\d+ (?:blue|red|green)(?:, \d+ (?:blue|red|green))*)", game)

        game_id_str: str = throws.pop(0)
        game_id: int = int(game_id_str.split(" ")[1].replace(":", ""))

        throws: List[List[str]] = list(
            map(lambda throw: throw.split(', '), throws))

        for throw in throws:
            for color_pair in throw:
                color_pair = color_pair.split(" ")

                maximum = cubes[color_pair[1]]

                if int(color_pair[0]) > maximum:
                    game_is_valid = False

        if game_is_valid:
            valid_game_ids.append(game_id)

    answer = sum(valid_game_ids)

    submit(answer, part="a", year=YEAR, day=DAY)


def part_two(input_data: str):
    input_data = input_data.splitlines()

    answer = 0

    for game in input_data:
        throws = re.findall(
            r"(Game \d+:|\d+ (?:blue|red|green)(?:, \d+ (?:blue|red|green))*)", game)
        throws.pop(0)

        throws: List[List[str]] = list(
            map(lambda throw: throw.split(', '), throws))

        color_pairs = {}

        for throw in throws:
            for color_pair in throw:
                color_pair = color_pair.split(" ")

                if color_pair[1] in color_pairs:
                    if color_pairs[color_pair[1]] < int(color_pair[0]):
                        color_pairs[color_pair[1]] = int(color_pair[0])
                else:
                    color_pairs[color_pair[1]] = int(color_pair[0])

        power = list(color_pairs.values())
        power = reduce(lambda item, accumulator: accumulator * item, power)

        answer += power

    submit(answer, part="b", year=YEAR, day=DAY)


part_one(puzzle.input_data)
part_two(puzzle.input_data)
