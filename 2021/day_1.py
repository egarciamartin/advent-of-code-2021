def parse_input(day):
    with open(f'inputs/{day}.txt') as file:
        lines = file.readlines()
        input = [int(line.strip()) for line in lines]
    return input


def part1(l):
    counter = 0
    prev = l[0]
    for item in l:
        if item > prev:
            counter += 1
        prev = item
    return counter


def part2(l):
    counter = 0
    sum_prev = l[0]
    for i in range(len(l)-2):
        sum_window = l[i] + l[i+1] + l[i+2]
        if i > 0 and sum_window > sum_prev:
            counter += 1
        sum_prev = sum_window
    return counter


if __name__ == '__main__':
    # Inputs
    test = parse_input('day1_test')
    input = parse_input('day1')

    # Part 1
    print(f'Part 1: Test input: {part1(test)}')
    print(f'Part 1: Real input: {part1(input)}')

    # Part 2
    print(f'Part 2: Test input: {part2(test)}')
    print(f'Part 2: Real input: {part2(input)}')
