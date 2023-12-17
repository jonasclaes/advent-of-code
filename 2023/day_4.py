from collections import defaultdict
from aocd import submit
from aocd.models import Puzzle

YEAR = 2023
DAY = 4

puzzle = Puzzle(year=YEAR, day=DAY)


def part_one(cards: str):
    answer = 0
    cards = cards.splitlines()

    # cards = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    # ]

    for card in cards:
        card = card.split(':')[1].split('|')
        winning_numbers = card[0].strip().split(' ')
        winning_numbers = list(
            filter(lambda value: value != '', winning_numbers))
        my_numbers = card[1].strip().split(' ')
        my_numbers = list(filter(lambda value: value != '', my_numbers))

        card_score = 0

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                if card_score == 0:
                    card_score = 1
                    continue

                card_score *= 2

        answer += card_score

        print(winning_numbers, my_numbers, card_score)

    print(f"Answer: {answer}")

    submit(answer, part="a", year=YEAR, day=DAY)


def part_two(cards: str):
    answer = 0
    cards = cards.splitlines()

    # cards = [
    #     "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    #     "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    #     "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    #     "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    #     "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    #     "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    # ]

    cards_dictionary = defaultdict(lambda: (0, [], []))

    for card in cards:
        card = card.split(':')
        card_number = int(card[0][5:])
        card = card[1].split('|')
        winning_numbers = card[0].strip().split(' ')
        winning_numbers = list(
            filter(lambda value: value != '', winning_numbers))
        my_numbers = card[1].strip().split(' ')
        my_numbers = list(filter(lambda value: value != '', my_numbers))

        cards_dictionary[card_number] = (
            card_number, winning_numbers, my_numbers)

    cards_to_be_processed = list(cards_dictionary.values())

    cards_processed = defaultdict(lambda: 0)

    for card in cards_to_be_processed:
        card_number = card[0]
        winning_numbers = card[1]
        my_numbers = card[2]

        matches = 0

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                matches += 1

        for i in range(card_number + 1, card_number + 1 + matches):
            cards_to_be_processed.append(cards_dictionary[i])

        cards_processed[card_number] += 1

        # print(card_number, winning_numbers, my_numbers, matches)

    answer = sum(cards_processed.values())

    print(f"Answer: {answer}")

    submit(answer, part="b", year=YEAR, day=DAY)


part_one(puzzle.input_data)
part_two(puzzle.input_data)
