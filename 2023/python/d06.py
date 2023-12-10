import pathlib
import math
from functools import reduce


def p1(time, distance):
    res = []
    for i in range(len(time)):
        a = -1
        b = time[i]
        c = - distance[i]
        res1 = math.ceil(( -b + math.sqrt(b**2 - (4*a*c) ) ) / (2*a))
        res2 = math.floor(( -b - math.sqrt(b**2 - (4*a*c) ) ) / (2*a))
        res.append(res2 - res1 + 1)

    return reduce(lambda x, y: x * y, res)

def p2(time, distance):
    a = -1
    b = time
    c = - distance
    res1 = math.ceil(( -b + math.sqrt(b**2 - (4*a*c) ) ) / (2*a))
    res2 = math.floor(( -b - math.sqrt(b**2 - (4*a*c) ) ) / (2*a))

    return res2 - res1 + 1

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    data = data.split('\n')
    time = list(filter(lambda s: s != '', data[0].split(' ')))
    time = list(map(int, time[1:]))

    distance = list(filter(lambda s: s != '', data[1].split(' ')))
    distance = list(map(int, distance[1:]))


    p1_res = p1(time, distance)
    print(p1_res)

    time = int(data[0].replace(' ', '').split(':')[1])
    distance = int(data[1].replace(' ', '').split(':')[1])

    p2_res = p2(time, distance)
    print(p2_res)
