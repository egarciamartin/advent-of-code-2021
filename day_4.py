import util
import numpy as np


def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()

    numbers = list(map(int, lines[0].split(",")))
    boards = list()
    j = 0
    board = np.zeros((5, 5))

    for i in range(1, len(lines)):
        line = lines[i].strip().split(" ")
        line = [int(el) for el in line if el != ""]
        if not line:  # list is empty
            board = (np.zeros((5, 5)))
            boards.append(board)
            j = 0
        else:
            board[j, :] = line
            j += 1

    return numbers, boards


def part1(numbers, boards):
    masks = [np.full((5, 5), False) for board in boards]
    winner = False
    i = 0
    score = 0
    while winner == False:
        number = numbers[i]
        for j, board in enumerate(boards):
            mask = board[:, :] == number
            masks[j] = masks[j] + mask
            sums = (np.sum(masks[j], axis=1), np.sum(masks[j], axis=0))
            if (5 in sums[0]) or (5 in sums[1]):
                winner = True
                s = np.sum(board * ~masks[j])
                score = number * s
        i += 1
    return int(score)


def part2(numbers, boards):
    masks = [np.full((5, 5), False) for board in boards]
    wins = [False for board in boards]
    winner = False
    i = 0
    score = 0
    while winner == False:
        number = numbers[i]
        for j, board in enumerate(boards):
            mask = board[:, :] == number
            masks[j] = masks[j] + mask
            sums = (np.sum(masks[j], axis=1), np.sum(masks[j], axis=0))
            if (5 in sums[0]) or (5 in sums[1]):
                if (sum(wins) == (len(wins) - 1)) and (wins[j] == False):
                    s = np.sum(board * ~masks[j])
                    score = number * s
                    winner = True
                else:
                    wins[j] = True
        i += 1
    return int(score)


if __name__ == '__main__':
    numbers_t, boards_t = parse_input('day4_test')
    numbers, boards = parse_input('day4')

    print(f"Part 1. Test: {part1(numbers_t, boards_t)}")
    print(f"Part 1. Real: {part1(numbers, boards)}")

    print(f"Part 2. Test: {part2(numbers_t, boards_t)}")
    print(f"Part 2. Real: {part2(numbers, boards)}")