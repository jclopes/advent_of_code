import pathlib

def opposit_direction(direction):
    res = None
    match direction:
        case 'w':
            res = 'e'
        case 'e':
            res = 'w'
        case 'n':
            res = 's'
        case 's':
            res = 'n'
    return res

def flow(from_dir, pipe):
    """Returns the direction we will exit the pipe
    if we enter the pipe from the from_dir direction.
    """
    to_dir = None
    match from_dir:
        case 'w':
            match pipe:
                case '-':
                    to_dir = 'e'
                case 'J':
                    to_dir = 'n'
                case '7':
                    to_dir = 's'

        case 'e':
            match pipe:
                case '-':
                    to_dir = 'w'
                case 'L':
                    to_dir = 'n'
                case 'F':
                    to_dir = 's'
        case 'n':
            match pipe:
                case '|':
                    to_dir = 's'
                case 'J':
                    to_dir = 'w'
                case 'L':
                    to_dir = 'e'
        case 's':
            match pipe:
                case '|':
                    to_dir = 'n'
                case '7':
                    to_dir = 'w'
                case 'F':
                    to_dir = 'e'
    return to_dir

def move_to(position, direction):
    """Return the new position after moving in the given direction."""
    x, y = position
    match direction:
        case 'w':
            x -= 1
        case 'e':
            x += 1
        case 'n':
            y -= 1
        case 's':
            y += 1
    return x, y

def parse_data(data):
    pipes = data.split('\n')
    pipes = [list(p.strip()) for p in pipes]
    return pipes

def find_start(pipes):
    """Returs the coordinates of the position of 'S'."""
    len_rows = len(pipes)
    len_cols = len(pipes[0])
    for row in range(len_rows):
        for col in range(len_cols):
            if 'S' == pipes[row][col]:
                return (col, row)
    return None

def find_connections(pipes, position):
    """Returns the directions that contain pipes
    that connect to the given 'position'.
    """
    connected = []
    col, row = position
    if flow('w', pipes[row][col + 1]) is not None:
        connected.append('e')
    if flow('e', pipes[row][col - 1]) is not None:
        connected.append('w')
    if flow('n', pipes[row + 1][col]) is not None:
        connected.append('s')
    if flow('s', pipes[row - 1][col]) is not None:
        connected.append('n')
    return connected

def pipe_at(pipes, position):
    x, y = position
    return pipes[y][x]

def trace_contour(pipes):
    position = find_start(pipes)
    connections = find_connections(pipes, position)
    # make first move
    position = move_to(position, connections[0])
    contour = [position]  # list of positions that define our shape
    from_dir = opposit_direction(connections[0])

    while pipe_at(pipes, position) != 'S':
        to_dir = flow(from_dir, pipe_at(pipes, position))
        position = move_to(position, to_dir)
        contour.append(position)
        from_dir = opposit_direction(to_dir)
    return contour

def p1(data):
    pipes = parse_data(data)
    contour = trace_contour(pipes)
    return len(contour) // 2

def can_flow_e(pipe_a, pipe_b):
    return pipe_a in ['-', 'F', 'L'] and pipe_b in ['-', '7', 'J']

def p2(data):
    pipes = parse_data(data)
    shape = set(trace_contour(pipes))

    # Convert S to a propper pipe
    sx, sy = find_start(pipes)
    sc = find_connections(pipes, (sx, sy))
    sc.sort()
    match sc:
        case ['e', 's']:
            pipes[sy][sx] = 'F'
        case ['s', 'w']:
            pipes[sy][sx] = '7'
        case ['e', 'w']:
            pipes[sy][sx] = '-'
        case ['n', 's']:
            pipes[sy][sx] = '|'
        case ['n', 'w']:
            pipes[sy][sx] = 'J'
        case ['e', 'n']:
            pipes[sy][sx] = 'L'

    len_rows = len(pipes)
    len_cols = len(pipes[0])
    inner_points = set()
    inside = False
    for y in range(len_rows):
        x = 0
        while x < len_cols:
            if inside and (x, y) not in shape:
                inner_points.add((x, y))
            elif (x, y) in shape:
                edge = [pipes[y][x]]
                while x+1 < len_cols and can_flow_e(pipes[y][x], pipes[y][x+1]) and (x+1, y) in shape:
                    x += 1
                    edge.append(pipes[y][x])
                if (edge[0] != 'L' or edge[-1] != 'J') and (edge[0] != 'F' or edge[-1] != '7'):
                    inside = not inside
            x += 1

    return len(inner_points)

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """
# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........
#     """.strip()

#     data = """
# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
#     """.strip()

#     data = """
# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
#     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
