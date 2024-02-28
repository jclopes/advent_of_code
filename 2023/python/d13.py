import pathlib

def parse_data(data):
    mirrors = data.split('\n\n')
    res = [[list(i.strip()) for i in m.split('\n')] for m in mirrors]
    return res

def find_vertical_reflect(mirror):
    """
    Possible out comes:
     - Full reflection left and right side are perfect reflections. Reflection point is in the middle.
     - Partial reflection: One side is a partial reflection of the other side. Reflection point is scwed to one side.
     - No reflection: No side is a reflection from the other. There could be still some identical lines.
    """
    found = False
    point = 0
    for idx in range(1, len(mirror[0])):
        for l in mirror:
            if l[0] != l[idx]:
                break
        else:
            return idx

    for idx in range(1, len(mirror[0])):
        for l in mirror:
            if l[0] != l[idx]:
                break
        else:
            return idx

    return None

def verify_reflection_vertical(mirror, center):
    return False

def verify_reflection_horizontal(mirror, center):
    return False

def find_horizontal_copy(mirror):
    return 0

def p1(data):
    sum = 0
    mirrors = parse_data(data)
    res = find_vertical_reflect(mirrors[1])
    return res

def p2(data):
    sum = 0
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
    """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
