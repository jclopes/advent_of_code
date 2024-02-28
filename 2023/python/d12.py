import pathlib

def parse_data(data):
    res = []
    lines = data.split('\n')
    for l in lines:
        springs, sum = l.split(' ')
        numbers = [int(n) for n in sum.split(',')]
        res.append((springs, numbers))
    return res

def p1(data):
    sum = 0
    res = parse_data(data)
    return res

def p2(data):
    sum = 0
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
#     """.strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
