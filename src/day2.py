def part1(file):
    double_chars = 0
    triple_chars = 0
    for word in file:
        sorted_word = ''.join(sorted(word))
        char_appearance = dict()
        for char in sorted_word:
            if char in char_appearance:
                char_appearance[char] = char_appearance[char] + 1
            else:
                char_appearance[char] = 1
        twice_found = False
        triple_found = False
        for char in char_appearance:
            if char_appearance[char] == 2 and not twice_found:
                double_chars += 1
                twice_found = True
            if char_appearance[char] == 3 and not triple_found:
                triple_chars += 1
                triple_found = True

            if twice_found and triple_found:
                break

    print("double chars: " + str(double_chars) + "; triple chars: " + str(triple_chars))
    print("result: " + str(double_chars * triple_chars))


def part2(file):
    words = list()
    for word in file:
        words.append(word.rstrip())
    for i in range(len(words)-2):
        i_word = words[i]
        for j in range(i+1, len(words)-1):
            j_word = words[j]
            if len(j_word) != len(i_word):
                continue
            if i_word == j_word:
                continue
            different_char_index = -1
            for index in range(0, len(i_word)):
                if i_word[index] != j_word[index]:
                    if different_char_index != -1:
                        different_char_index = -1
                        break
                    different_char_index = index
            if different_char_index != -1:
                print(i_word[:different_char_index] + "" + i_word[different_char_index+1:])
                return


if __name__ == '__main__':
    file = open('../assets/day2-input.txt', 'r')
    part1(file)
    file.seek(0)
    part2(file)
