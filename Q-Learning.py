import numpy as np
import random
import sys
sys.setrecursionlimit(1000000)
Q = np.zeros((6, 6))
R = np.asarray([[-1, -1, -1, -1, 0, -1],
                [-1, -1, -1, 0, -1, 100],
                [-1, -1, -1, 0, -1, -1],
                [-1, 0, 0, -1, 0, -1],
                [0, -1, -1, 0, -1, 100],
                [-1, 0, -1, -1, 0, 100]])


def Q_learing(s, a, R, Q):
    # while a != 5:
    Q[s, a] = R[s, a] + 0.8 * max(Q[a, :])
    #s = a
    #a = random.randint(0, 5)
    # while R[s, a] < 0:
    #a = random.randint(0, 5)
    #Q_learing(s, a, R, Q)

    # return Q


count = 0
while count < 2000:
    s = random.randint(0, 5)
    a = random.randint(0, 5)
    while R[s, a] < 0:
        a = random.randint(0, 5)
    Q_learing(s, a, R, Q)
    count += 1
print(Q / 5)
