from itertools import cycle


def part1(frequencies):
    result = 0
    for frequency in frequencies:
        result += int(frequency)

    print(result)


def part2(frequencies):
    results = {0}
    result = 0
    for frequency in cycle(frequencies):
        result += int(frequency)
        if result in results:
            print(result)
            break
        results.add(result)


if __name__ == '__main__':
    file = open('../assets/input-day1.txt', 'r')
    part1(file)
    file.seek(0)
    part2(file)

