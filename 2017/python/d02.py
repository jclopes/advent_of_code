import pathlib

def min_max(row):
    min = row[0]
    max = row[0]
    for i in row:
        if min > i: min = i
        if max < i: max = i
    return (min, max)

def parse_row(line):
    """Conversts a string of numbers separated by spaces
    into a list of ints."""
    digits = line.strip().split('\t')
    ints = map(int, digits)
    return list(ints)

def p1(data):
    sum = 0
    for line in data.split('\n'):
        row = parse_row(line)
        min, max = min_max(row)
        sum += max - min
    return sum

def find_divisible(row):
    row.sort()
    row.reverse()
    res = 0
    for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
            if divisible(row[i], row[j]):
                res = row[i] // row[j]
                break
        if res != 0: break
    return res

def divisible(x, y):
    return (x % y) == 0

def p2(data):
    sum = 0
    for line in data.split('\n'):
        row = parse_row(line)
        quotient = find_divisible(row)
        sum += quotient
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()
    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
