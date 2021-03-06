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


def part1(input, part2=False):

    numbers, boards = input
    masks = [np.full((5, 5), False) for board in boards]
    wins = [False for board in boards]
    winner = False
    i = 0
    while winner == False:
        number = numbers[i]
        for j, board in enumerate(boards):
            mask = board[:, :] == number
            masks[j] = masks[j] + mask
            if np.any((np.all(masks[j], axis=0), np.all(masks[j], axis=1))):
                if part2:
                    if (sum(wins) == (len(wins) - 1)) and (wins[j] == False):
                        s = np.sum(board * ~masks[j])
                        winner = True
                    else:
                        wins[j] = True
                else:
                    winner = True
                    s = np.sum(board * ~masks[j])
        i += 1
    return int(number * s)


def part2(input):
    return part1(input, part2=True)


if __name__ == '__main__':
    test = parse_input('day4_test')
    input = parse_input('day4')

    print(f"Part 1. Test: {part1(test)}")
    print(f"Part 1. Real: {part1(input)}")

    print(f"Part 2. Test: {part2(test)}")
    print(f"Part 2. Real: {part2(input)}")
