import math
from math import *


def a(P, W, H, a):
    S = min(W, H)
    rows = [math.ceil(a_i / int(W / S)) for a_i in a]
    Row = sum(rows)
    pages = math.ceil(Row / int(H / S))
    while pages > P:
        S = S - 1
        rows = [math.ceil(a_i / int(W / S)) for a_i in a]
        Row = sum(rows)
        pages = math.ceil(Row / int(H / S))
    print(S)


def test(line1, line2):
    max_S = 0

    [N, P, W, H] = [int(x) for x in line1.strip().split()]
    a = [int(arg) for arg in line2.strip().split()]

    for S in range(min(W, H), 0, -1):
        cols = floor(W / S)
        row = floor(H / S)
        lines = [ceil(ai / cols) for ai in a]
        rows = sum(lines)
        pages = int(ceil(rows / row))
        if pages <= P and S > max_S:
            max_S = S
    print(max_S)


a(30, 20, 20, [50, 100, 200, 100, 400, 50, 100, 200, 100, 400])
test('10 30 20 20', '50 100 200 100 400 50 100 200 100 400')
