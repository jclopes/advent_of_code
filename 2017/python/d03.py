import pathlib
import math

def p1(data):
    """Each new layer has size = previous_layer_side + 2.
    The nth layer has side = (n * 2) - 1.
    The max value of a layer is it's side^2.
    The Manhatan distance to the center is the distance to the
    center of the side plus the number of layers.

    The sqrt of the input gives us an aproximate value of
    the side that is lower that the correct layer side length.
    The correct layer side length will the nearst odd number
    higher than the sqrt of the input.
    Calculate the distance to the max_layer value that is
    always on the bottom right side.
    Subtract the side length minus one until our value is smaller
    then the side length.
    Calculate the distance to the mid point of the side.
    Add the number of the layer to obtain the final result.
    """
    n = int(data)
    side = math.ceil(math.sqrt(n))
    if (side % 2) == 0: side += 1
    level_max = math.pow(side, 2)
    delta = level_max - n
    half_side = side // 2
    while delta > (side - 1):
        delta -= (side - 1)

    return abs(half_side - delta) + half_side

def p2(data):
    n = int(data)
    return n

def main(input_file):
    data = pathlib.Path(input_file).read_text().strip()
    p1_res = p1(data)
    print(p1_res)

    import pdb; pdb.set_trace()

    p2_res = p2(data)
    print(p2_res)
