import pathlib


def p1(data):
    sum = 0
    for line in data.split('\n'):
        digits = list(filter(str.isdigit, line))
        pair = digits[0]+digits[-1]
        sum += int(pair)
    return sum

def text2digit(line):
    """
    Intentionally keep all but the first letter in for future matching
    to support strings that overlap. ex: "oneight" => 18
    """
    res = ""
    i_max = len(line)
    i = 0
    while i < i_max:
        if i+3 <= i_max and line[i:i+3] == "one":
            res += "1"
        elif i+3 <= i_max and line[i:i+3] == "two":
            res += "2"
        elif i+5 <= i_max and line[i:i+5] == "three":
            res += "3"
        elif i+4 <= i_max and line[i:i+4] == "four":
            res += "4"
        elif i+4 <= i_max and line[i:i+4] == "five":
            res += "5"
        elif i+3 <= i_max and line[i:i+3] == "six":
            res += "6"
        elif i+5 <= i_max and line[i:i+5] == "seven":
            res += "7"
        elif i+5 <= i_max and line[i:i+5] == "eight":
            res += "8"
        elif i+4 <= i_max and line[i:i+4] == "nine":
            res += "9"
        else:
            res += line[i]
        i += 1
    return res

def p2(data):
    sum = 0
    for line in data.split('\n'):
        line_digits = text2digit(line)
        digits = list(filter(str.isdigit, line_digits))
        pair = digits[0]+digits[-1]
        sum += int(pair)
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()
    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
