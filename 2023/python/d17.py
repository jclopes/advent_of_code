import pathlib

def parse_data(data):
    maze = data.split('\n')
    res = []
    for line in maze:
        r = map(int, line)
        res.append(list(r))
    return res

def possible_moves(maze, position, last3moves):
    maxx = len(maze[0])
    maxy = len(maze)
    x, y = position
    change_direction = False
    if last3moves[0] == last3moves[1] and last3moves[1] == last3moves[2]:
        change_direction = True

    res = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]

    # remove reverse move (180 turn) and enforce direction change
    match last3moves[2]:
        case 'N':
            res.remove((x, y+1))
            if change_direction:
                res.remove((x, y-1))
        case 'S':
            res.remove((x, y-1))
            if change_direction:
                res.remove((x, y+1))
        case 'W':
            res.remove((x+1, y))
            if change_direction:
                res.remove((x-1, y))
        case 'E':
            res.remove((x-1, y))
            if change_direction:
                res.remove((x+1, y))
    # remove out of bounds options
    res = list(filter(\
        lambda p: p[0] >= 0 and p[1] >= 0 and p[0] < maxx and p[1] < maxy,\
        res))
    return res

def search(maze, start, finish):
    sx, sy = start
    fx, fy = finish
    cost = 0

    return cost

def p1(data):
    sum = 0
    maze = parse_data(data)

    mem = dict()
    def mem_possible_moves(maze, position, last3moves):
        if not (position, last3moves) in mem:
            res = possible_moves(maze, position, last3moves)
            mem[(position, last3moves)] = res
        return mem[(position, last3moves)]

    res = mem_possible_moves(maze,(0,12), tuple([None,None,None]))
    # print(mem)
    return res

def p2(data):
    sum = 0
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    data = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
    """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
