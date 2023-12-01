# Advent of Code Solutions

## Introduction
Welcome to my repository of solutions for the Advent of Code challenges! Advent of Code is an annual set of Christmas-themed programming puzzles that can be solved in any programming language. This repository contains my personal solutions, aiming to explore and improve my problem-solving and programming skills.

## Setup and Installation
Before running the solutions, ensure you have Python installed on your machine. Then, install the `advent-of-code-data` package, which I use for fetching input data and submitting solutions. You can install this package via pip:

```bash
pip install advent-of-code-data
```

## Usage
To use the `advent-of-code-data` package, you need to set up your session token to fetch your personal puzzle inputs and submit solutions. Follow these steps:

1. Log in to your Advent of Code account.
2. Get your session cookie from the browser.
3. Export this session cookie as an environment variable:

```bash
export AOC_SESSION='your-session-token'
```

4. Use the package in your Python scripts to get the puzzle input:

```python
from advent_of_code_data import get_data

day = 1
year = 2021
input_data = get_data(day=day, year=year)
```

5. After solving the puzzle, you can submit your solution:

```python
from advent_of_code_data import submit

answer = 'your-solution'
submit(answer=answer, day=day, year=year, level=1)
```

## Structure of Repository

- `Year20XX`: One folder for each year of the Advent of Code challenges.
  - `day_1.py`: Solution for Day 1.
  - `day_2.py`: Solution for Day 2.
  - ...
  - `day_25.py`: Solution for Day 25.
  - `README.md`: A brief overview of the solutions, including any unique strategies or approaches used.

Each script (`day_X.py`) is a standalone solution for that day's puzzle. You can run each script individually to see the solutions for each day.

For example, to run the solution for Day 1 of the year 2023, navigate to the `Year2023` folder and run:

```bash
python day_1.py
```

## Contributions
While this repository is primarily for my personal learning and exploration, any suggestions or improvements are welcome! Please feel free to open an issue or a pull request.

## License
This project is open-sourced under the [MIT License](LICENSE).

## Acknowledgments
A big thank you to the creators and maintainers of the Advent of Code for creating such engaging and educational challenges!
