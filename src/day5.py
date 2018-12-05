def part1(polymer):
    result = ""
    prev_char = ''
    index = 0
    while True:
        char = polymer.read(1)
        if not char:
            break
        if prev_char == '':
            prev_char = char
        index += 1
        result += char
        if index < 2:
            continue
        if abs(ord(char) - ord(prev_char)) == 32:
            result = result[:index-2]
            index -= 2
            if len(result) > 0:
                prev_char = result[-1]
            else:
                prev_char = ''
            continue
        prev_char = char
    print(len(result))


def remove_reactions(polymer):
    result = ""
    prev_char = ''
    index = 0
    for char in polymer:
        if not char:
            break
        if prev_char == '':
            prev_char = char
        index += 1
        result += char
        if index < 2:
            continue
        if abs(ord(char) - ord(prev_char)) == 32:
            result = result[:index - 2]
            index -= 2
            if len(result) > 0:
                prev_char = result[-1]
            else:
                prev_char = ''
            continue
        prev_char = char
    return result


def part2(polymer):
    result = ""
    prev_char = ''
    index = 0
    removed_units = {}
    while True:
        char = polymer.read(1)
        if not char:
            break
        if prev_char == '':
            prev_char = char
        index += 1
        result += char
        if index < 2:
            continue
        if abs(ord(char) - ord(prev_char)) == 32:
            if char not in removed_units and prev_char not in removed_units:
                removed_units[prev_char] = char
        prev_char = char

    shortest_length = len(result)
    for unit in removed_units:
        temp = result.replace(unit, '').replace(removed_units[unit], '')
        removed_reactions = remove_reactions(temp)
        if len(removed_reactions) < shortest_length:
            shortest_length = len(removed_reactions)
    print(shortest_length)


if __name__ == '__main__':
    file = open('../assets/day5-input.txt', 'r')
    part1(file)
    file.seek(0)
    part2(file)
