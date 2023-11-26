#! /bin/env python

import sys
import pathlib

def p1(data):
    sum = 0
    for i in range(len(data)):
        j = (i + 1) % len(data)
        if data[i] == data[j]:
            sum += int(data[i])
    return sum

def p2(data):
    data_len = len(data)
    offset = data_len // 2
    sum = 0
    for i in range(data_len):
        j = (i + offset) % data_len
        if data[i] == data[j]:
            sum += int(data[i])
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()
    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)

if __name__ == '__main__':
    main()