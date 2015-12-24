import Define
import random
import numpy as np


def initMatrix():
    x = np.empty([Define.M, Define.N], int)
    for m in range(Define.M):
        for n in range(Define.N):
            x[m, n] = randomOne()
    return x


def randomOne():
    return random.getrandbits(1)
