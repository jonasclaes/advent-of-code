from collections import defaultdict
from functools import reduce
import re
from typing import List
from aocd import submit
from aocd.models import Puzzle

YEAR = 2023
DAY = 3

puzzle = Puzzle(year=YEAR, day=DAY)


def part_one(input_data: str):
    input_data = input_data.splitlines()

    symbols = set("*+#$/&-=@%")

    sum_parts = 0

    def in_bounds(x, y, max_x, max_y):
        return 0 <= x < max_x and 0 <= y < max_y

    def is_adjacent_to_symbol(x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if in_bounds(x + dx, y + dy, len(input_data), len(input_data[0])) and input_data[x + dx][y + dy] in symbols:
                    return True
        return False

    for i in range(len(input_data)):
        j = 0
        while j < len(input_data[i]):
            if input_data[i][j].isdigit():
                num_str = input_data[i][j]
                k = j + 1

                while k < len(input_data[i]) and input_data[i][k].isdigit():
                    num_str += input_data[i][k]
                    k += 1

                if any(is_adjacent_to_symbol(i, j + d) for d in range(len(num_str))):
                    sum_parts += int(num_str)

                j = k
            else:
                j += 1

    submit(sum_parts, part="a", year=YEAR, day=DAY)


def part_two(input_data: str):
    input_data = input_data.splitlines()

    schema_height = len(input_data) - 1
    schema_length = len(input_data[0]) - 1

    def find_gear_positions(current_x: int, current_y: int, number_chunk_length: int) -> set[tuple[int, int]]:
        x_start = max(0, current_x - number_chunk_length)
        y_start = max(0, current_y - 1)
        x_end = min(schema_length, current_x + 2)
        y_end = min(schema_height, current_y + 2)

        return {
            (y, x) for y in range(y_start, y_end)
            for x in range(x_start, x_end) if input_data[y][x] == "*"
        }

    gear_position_number_map = defaultdict(list)

    for y, line in enumerate(input_data):
        number_chunk = ""
        for x, character in enumerate(line):
            if character.isdigit():
                number_chunk += character

                if x == schema_length or not line[x + 1].isdigit():
                    for position in find_gear_positions(x, y, len(number_chunk)):
                        gear_position_number_map[position].append(
                            int(number_chunk))

                    number_chunk = ""

    answer = sum((gear_position[0] * gear_position[1]
                 for gear_position in gear_position_number_map.values() if len(gear_position) == 2))

    submit(answer, part="b", year=YEAR, day=DAY)


part_one(puzzle.input_data)
part_two(puzzle.input_data)
