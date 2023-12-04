import pathlib


def parse_extraction(extraction):
    red = 0
    green = 0
    blue = 0
    for e in extraction.split(','):
        amount, color = e.strip().split(' ')
        amount = int(amount)
        match color:
            case 'red':
                if amount > red: red = amount
            case 'green':
                if amount > green: green = amount
            case 'blue':
                if amount > blue: blue = amount
    return(red, green, blue)

def is_possible_cubes(game):
    max_red = 12
    max_green = 13
    max_blue = 14
    for g in game.split(';'):
        red, green, blue = parse_extraction(g)
        if red > max_red or green > max_green or blue > max_blue:
            return False
    return True

def p1(data):
    sum = 0
    for line in data.split('\n'):
        id, cubes = line.split(':')
        id = id.strip().split(' ')
        id = int(id[1])
        if is_possible_cubes(cubes):
            sum += id
    return sum

def power_game(game):
    max_red = 0
    max_green = 0
    max_blue = 0
    for g in game.split(';'):
        red, green, blue = parse_extraction(g)
        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue
    return max_red * max_green * max_blue

def p2(data):
    sum = 0
    for line in data.split('\n'):
        id, cubes = line.split(':')
        id = id.strip().split(' ')
        id = int(id[1])
        sum += power_game(cubes)
    return sum

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()

    p1_res = p1(data)
    print(p1_res)

    p2_res = p2(data)
    print(p2_res)
