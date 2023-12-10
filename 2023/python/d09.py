import pathlib

def parse_data(data):
    lines = data.split('\n')

    res = []
    for l in lines:
        row = [int(n) for n in l.split(' ')]
        res.append(row)
    return res

def is_zeros(row):
    for i in row:
        if i != 0:
            return False
    return True

def calculate(row):
    idx = 0
    new_row = []
    while idx+1 < len(row):
        new_row.append(row[idx+1] - row[idx])
        idx += 1
    if is_zeros(new_row):
        res = row[-1]
    else:
        res = calculate(new_row) + row[-1]
    return res

def p1(data):
    data = parse_data(data)
    res = []
    for row in data:
        res.append(calculate(row))
    return sum(res)

def calculate2(row):
    idx = 0
    new_row = []
    while idx+1 < len(row):
        new_row.append(row[idx+1] - row[idx])
        idx += 1
    if is_zeros(new_row):
        res = row[0]
    else:
        res = row[0] - calculate2(new_row)
    return res


def p2(data):
    data = parse_data(data)
    res = []
    for row in data:
        res.append(calculate2(row))
    return sum(res)

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
#     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
