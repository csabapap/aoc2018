import sys


def create_coordinates_list(coordinates):
    coordinates_list = []
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = 0
    max_y = 0
    for coordinate in coordinates:
        first_part = coordinate.rstrip().split('@')
        plan_id = first_part[0]
        second_part = first_part[1].split(':')
        xy = second_part[0]
        x = int(xy.split(',')[0])
        y = int(xy.split(',')[1])
        if x < min_x:
            min_x = x

        if y < min_y:
            min_y = y

        size = second_part[1]
        split = size.split('x')
        w = int(split[0])
        h = int(split[1])

        if x + w > max_x:
            max_x = x + w

        if y + h > max_y:
            max_y = y + h
        coordinates_list.append({'id': plan_id, 'coordinate': xy, 'size': size})
    print(f"canvas size: {max_x}x{max_y}")
    return {"coordinates": coordinates_list, 'size': f"{max_x}x{max_y}"}


def create_canvas(result):
    coordinates = result['coordinates']
    size = result['size']
    rows = int(size.split('x')[0])
    columns = int(size.split('x')[1])

    canvas = [[0 for x in range(rows)] for x in range(columns)]

    for i in range(0, len(coordinates)):
        coordinate = coordinates[i]
        x = int(coordinate['coordinate'].split(',')[0])
        y = int(coordinate['coordinate'].split(',')[1])
        w = int(coordinate['size'].split('x')[0])
        h = int(coordinate['size'].split('x')[1])

        for r in range(x, x + w):
            for c in range(y, y + h):
                canvas[r][c] += 1
    return canvas


def part1(canvas):
    overlaps = 0
    for i in range(len(canvas)):
        for j in range(len(canvas[0])):
            if canvas[i][j] > 1:
                overlaps += 1
    print(overlaps)


def part2(result):
    coordinates = result['coordinates']
    canvas = create_canvas(result)

    for i in range(0, len(coordinates)):
        coordinate = coordinates[i]
        x = int(coordinate['coordinate'].split(',')[0])
        y = int(coordinate['coordinate'].split(',')[1])
        w = int(coordinate['size'].split('x')[0])
        h = int(coordinate['size'].split('x')[1])

        overlap_found = False
        for r in range(x, x + w):
            if overlap_found:
                break
            for c in range(y, y + h):
                if canvas[r][c] > 1:
                    overlap_found = True
                    break
        if not overlap_found:
            print(coordinate['id'])
            return


if __name__ == '__main__':
    file = open("../assets/day3-input.txt", 'r')
    part1(create_canvas(create_coordinates_list(file)))
    file.seek(0)
    part2(create_coordinates_list(file))
