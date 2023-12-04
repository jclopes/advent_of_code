import pathlib


def score(win_numbers, have_numbers):
    res = 0
    sum = 0
    for i in have_numbers:
        if i in win_numbers:
            sum += 1
    if sum > 0:
        res = 2**(sum - 1)
    return res

def p1(data):
    sum = 0
    for line in data.split('\n'):
        id, card = line.split(':')
        win_numbers, have_numbers = card.split('|')

        win_numbers = filter(str.isnumeric, win_numbers.strip().split(' '))
        win_numbers = list(map(int, win_numbers))

        have_numbers = filter(str.isnumeric, have_numbers.strip().split(' '))
        have_numbers = list(map(int, have_numbers))

        sum += score(win_numbers, have_numbers)

    return sum

def matches(win_numbers, have_numbers):
    sum = 0
    for i in have_numbers:
        if i in win_numbers:
            sum += 1
    return sum

def p2(data):
    id = 0
    cards = dict()
    for line in data.split('\n'):
        id += 1
        if id not in cards:
            cards[id] = 1

        _card_id, card = line.split(':')
        win_numbers, have_numbers = card.split('|')

        win_numbers = filter(str.isnumeric, win_numbers.strip().split(' '))
        win_numbers = list(map(int, win_numbers))

        have_numbers = filter(str.isnumeric, have_numbers.strip().split(' '))
        have_numbers = list(map(int, have_numbers))

        count = matches(win_numbers, have_numbers)
        for i in range(count):
            idx = id+1+i
            if idx not in cards:
                cards[idx] = 1
            cards[idx] += cards[id]

    return sum(cards.values())

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

#     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
