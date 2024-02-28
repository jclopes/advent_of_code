import pathlib

def parse_data(data):
    maze = data.split('\n')
    return maze

def find_start(maze):
    """Returs the coordinates of the position of 'S'."""
    len_rows = len(maze)
    len_cols = len(maze[0])
    for row in range(len_rows):
        for col in range(len_cols):
            if 'S' == maze[row][col]:
                return (col, row)
    return None

def possible_moves(maze, position):
    maxx = len(maze[0])
    maxy = len(maze)
    x, y = position
    res = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    res = list(filter(\
        lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < maxx and p[1] < maxy,\
        res))
    res = list(filter(lambda p: maze[p[1]][p[0]] != '#', res))
    return res

def expand(maze, sources):
    res = []
    for s in sources:
        res += possible_moves(maze, s)
    return set(res)

def p1(data):
    maze = parse_data(data)
    spos = find_start(maze)

    res = set()
    res.add(spos)
    for i in range(64):
        res = expand(maze, res)

    return len(res)

def possible_moves2(maze, visited, position):
    x, y = position
    res = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    def is_not_rock(position):
        maxx = len(maze[0])
        maxy = len(maze)
        x, y = position
        x %= maxx
        y %= maxy
        return maze[y][x] != '#'

    res = list(filter(lambda r: is_not_rock(r) and r not in visited, res))
    return res

def expand2(maze, visited, sources):
    res = []
    maxx = len(maze[0])
    maxy = len(maze)
    for s in sources:
        res += possible_moves2(maze, visited, s)

    return set(res)


def p2(data):
    """
    The current solution will find the right answer but too slow.
    Might take years to terminate.
    The good solution needs to take advantage of the fact that the board
    will repeat it self thousunds or even millions of times.
    Some assumptions can be made about the size of the board and the
    number of steps ratio.
    The final shape of the board will be a diamond.
    The center of the diamond will be a repeting pattern.
    The perimeter of the board will also be a repeating pattern.
    The diagonals of the perimeter will be composed of boards that are not
    totally full.
    To get the final answer we just need to calculate the boards at the
    diagonals and a couple of the central boards. Then multiply that with the
    size of the board.
    """
    maze = parse_data(data)
    spos = find_start(maze)

    res = 0
    sources = set([spos])
    visited = set()
    steps = 10000 #26501365
    save = True
    if steps % 2 == 0:
        res += len(sources)
        save = not save
    for i in range(steps):
        temp = expand2(maze, visited, sources)
        visited = sources.copy()
        sources = temp
        if save:
            res += len(sources)
        save = not save

    return res

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """
# ...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........
#     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
