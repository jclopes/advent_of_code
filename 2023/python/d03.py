import pathlib


def symbol_expand(symbol, max_col, max_row):
    def is_valid(pair):
        x, y = pair
        if x < 0 or y < 0 or x > max_col or y > max_row:
            return False
        return True

    x, y = symbol
    res = [(x, y),
        (x - 1, y),
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1)]
    return list(filter(is_valid, res))

def p1(data):
    """
    Map integer to cells they ocupy.
    Include integers that any cells they occupy is neighbor
    to a cel with a symbol.
    """
    row = 0
    sum = 0
    symbols = set()
    number_cells = {}
    matrix = data.split('\n')
    max_col = len(matrix[0])
    max_row = len(matrix)
    for line in matrix:
        line = line.strip()
        x = 0
        while x < max_col:
            digit = ''
            cells = []
            if str.isnumeric(line[x]):
                while x < max_col and str.isnumeric(line[x]):
                    digit += line[x]
                    cells.append((row, x))
                    x += 1
                if int(digit) not in number_cells:
                    number_cells[int(digit)] = []
                number_cells[int(digit)].append(cells)
            elif line[x] != '.':
                symbol_range = symbol_expand((row, x), max_col, max_row)
                symbols.update(symbol_range)
                x += 1
            else:
                x += 1
        row += 1

    for n in number_cells:
        for j in number_cells[n]:
            for c in j:
                if c in symbols:
                    sum += n
                    break
    return sum

def p2(data):
    id = 0
    row = 0
    sum = 0
    gears = []
    id_number = {}
    number_cells = {}
    matrix = data.split('\n')
    max_col = len(matrix[0])
    max_row = len(matrix)
    for line in matrix:
        line = line.strip()
        x = 0
        while x < max_col:
            digit = ''
            if str.isnumeric(line[x]):
                while x < max_col and str.isnumeric(line[x]):
                    digit += line[x]
                    number_cells[(row, x)] = id
                    x += 1
                id_number[id] = int(digit)
                id += 1
            elif line[x] == '*':
                gears.append((row, x))
                x += 1
            else:
                x += 1
        row += 1

    for g in gears:
        numbers_ids = set()
        for pos in symbol_expand(g, max_col, max_row):
            if pos in number_cells:
                numbers_ids.add(number_cells[pos])
        if len(numbers_ids) == 2:
            a, b = numbers_ids
            sum += id_number[a] * id_number[b]

    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    # data = """467....114
    #     ...*......
    #     ..35..633.
    #     ......#...
    #     617*......
    #     .....+.58.
    #     ..592.....
    #     ......755.
    #     ...$.*....
    #     .664.598.."""

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
