import pathlib

def lr2idx(direction):
    res = 0
    if direction == 'R':
        res = 1
    return res

def parse_data(data):
    path, rest = data.split('\n\n')
    path = list(map(lr2idx, path))

    graph = {}
    for line in rest.split('\n'):
        line.strip()
        pos, nodes = line.split(' = ')
        pos = pos.strip()
        l, r = nodes.split(',')
        l = l[1:].strip()
        r = r[:-1].strip()
        graph[pos] = (l, r)

    return (path, graph)

def p1(data):
    path, graph = parse_data(data)

    steps = 0
    pos = 'AAA'
    while pos != 'ZZZ':
        s = steps % len(path)
        pos = graph[pos][path[s]]
        steps += 1

    return steps

def is_div(num, nlist):
    res = True
    for n in nlist:
        if num % n != 0:
            res = False
            break
    return res

def p2(data):
    path, graph = parse_data(data)

    pos = list(filter(lambda g: g[2] == 'A', graph))
    loops = []
    for p in pos:
        steps = 0
        while p[2] != 'Z':
            s = steps % len(path)
            p = graph[p][path[s]]
            steps += 1
        loops.append(steps)

    big_loop = max(loops)
    factor = 1
    while not is_div(big_loop * factor, loops):
        factor += 1
    return factor * big_loop

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    # data = """
    #     LLR

    #     AAA = (BBB, BBB)
    #     BBB = (AAA, ZZZ)
    #     ZZZ = (ZZZ, ZZZ)
    # """.strip()

    # data = """
    #     RL

    #     AAA = (BBB, CCC)
    #     BBB = (DDD, EEE)
    #     CCC = (ZZZ, GGG)
    #     DDD = (DDD, DDD)
    #     EEE = (EEE, EEE)
    #     GGG = (GGG, GGG)
    #     ZZZ = (ZZZ, ZZZ)
    # """.strip()

    # data = """
    #     LR

    #     11A = (11B, XXX)
    #     11B = (XXX, 11Z)
    #     11Z = (11B, XXX)
    #     22A = (22B, XXX)
    #     22B = (22C, 22C)
    #     22C = (22Z, 22Z)
    #     22Z = (22B, 22B)
    #     XXX = (XXX, XXX)
    # """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
