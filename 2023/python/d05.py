import pathlib


def parse_seeds(seeds):
    res = seeds.split(' ')[1:]
    res = list(map(int, res))
    return res

def parse_rule(rule):
    r = list(map(int, rule.split(' ')))
    source_range = (r[1], r[1] + r[2] - 1)
    destination_start = r[0]

    return [source_range, destination_start]

def parse_data(data):

    functions = {}

    sections = data.split('\n\n')
    for s in sections[1:]:
        function = s.split('\n')
        function = list(map(str.strip, function))
        fun_name = function[0].split(' ')[0]
        fun_rules = list(map(parse_rule, function[1:]))
        functions[fun_name] = fun_rules

    seeds = parse_seeds(sections[0])

    return seeds, functions

def apply_fun(value, fun):
    res = value
    for r in fun:
        if value >= r[0][0] and value <= r[0][1]:
            res = r[1] + (value - r[0][0])
            break
    return res

def p1(data):
    seeds, functions = parse_data(data)

    locations = []
    for s in seeds:
        res = s
        for f in functions:
            res = apply_fun(res, functions[f])

        locations.append(res)

    locations.sort()
    return locations[0]

### ### ###

def parse_seeds2(seeds):
    res = seeds.split(' ')[1:]
    res = list(map(int, res))

    res = list(zip(res[::2], res[1::2]))

    return res

def parse_data2(data):

    functions = []

    sections = data.split('\n\n')
    for s in sections[1:]:
        function = s.split('\n')
        function = list(map(str.strip, function))
        fun_name = function[0].split(' ')[0]
        fun_rules = list(map(parse_rule, function[1:]))
        functions.append(fun_rules)

    seeds = parse_seeds2(sections[0])

    return seeds, functions

def get_min_location(seeds_start, seeds_len, functions):

    min_location = None
    s = seeds_start
    while s < seeds_start + seeds_len:
        res = s
        for f in functions:
            res = apply_fun(res, f)

        if min_location == None or min_location > res:
            min_location = res
        s += 1

    return min_location


def p2(data):
    """
    This solution will take ~4h to terminate.
    Possible Alternatives:
      * backwards search: Apply the functions in reverse order and only use
                          the lower range from the locations.
      * Instead of using individual seeds in the calculations use ranges.
            A range of values might need to be bronken into multiple ranges
            when passed to the next function, and so on.
    """
    seeds_range, functions = parse_data2(data)

    locations = []
    for s, l in seeds_range:
        location = get_min_location(s, l, functions)
        locations.append(location)

    locations.sort()
    return locations[0]

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    data = """
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
        """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
