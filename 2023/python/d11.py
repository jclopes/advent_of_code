import pathlib

def parse_data(data):
    lines = data.split('\n')

    lines = [list(l) for l in lines]

    rows = []
    for l in range(len(lines)):
        if '#' not in lines[l]:
            rows.append(l)

    cols = []
    for c in range(len(lines[0])):
        for r in range(len(lines)):
            if '#' == lines[r][c]:
                break
        else:
            cols.append(c)

    return lines, rows, cols

def count_lesser(list_num, treshold):
    res = list(filter(lambda x: x < treshold, list_num))
    return len(res)

def get_galaxies(galaxy_map, double_rows, double_cols):
    galaxies = []
    for r in range(len(galaxy_map)):
        for c in range(len(galaxy_map[0])):
            if galaxy_map[r][c] == '#':
                x = count_lesser(double_cols, c) + c
                y = count_lesser(double_rows, r) + r
                galaxies.append((x, y))
    return galaxies

def distance(p1, p2):
    res = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # print(p1, p2, res)
    return res

def p1(data):
    galaxy_map, double_rows, double_cols = parse_data(data)
    galaxies = get_galaxies(galaxy_map, double_rows, double_cols)
    res = []
    for idx in range(len(galaxies) - 1):
        for g in galaxies[idx + 1:]:
            res.append(distance(galaxies[idx], g))

    print(len(res))
    return sum(res)

def get_galaxies2(galaxy_map, double_rows, double_cols, ratio):
    galaxies = []
    for r in range(len(galaxy_map)):
        for c in range(len(galaxy_map[0])):
            if galaxy_map[r][c] == '#':
                x = (count_lesser(double_cols, c)*(ratio -1)) + c
                y = (count_lesser(double_rows, r)*(ratio -1)) + r
                galaxies.append((x, y))
    return galaxies

def p2(data):
    galaxy_map, double_rows, double_cols = parse_data(data)
    galaxies = get_galaxies2(galaxy_map, double_rows, double_cols, 1000000)
    res = []
    for idx in range(len(galaxies) - 1):
        for g in galaxies[idx + 1:]:
            res.append(distance(galaxies[idx], g))

    print(len(res))
    return sum(res)

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
#     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
