# run in python 3

import numpy as np
import os, sys, json
import math




def main(theta, alpha):

    #constants that change with use
    MASS = 1
    N = 4
    ALPHA = 0.5
    RADIUS = 1

    angles = [math.pi / 3, math.pi * 2 / 3, math.pi * 4 / 3, math.pi * 5/3]
    C = []

    C.append([-math.sin(i) for i in angles])
    C.append([math.cos(i) for i in angles])
    C.append([1/ALPHA for i in range(N)])

    C = np.array(C)
    print(C)
    _C = np.linalg.pinv(C)
    print(_C)
    A = getCartesianAcceleration(theta)
    A.append(alpha)
    _A = np.matrix(A).transpose()
    print(_A)

    print(np.dot(_C, _A))


def getCartesianAcceleration(theta):
    return [math.cos(theta), math.sin(theta)] # [a_x, a_y]


main(0, 0)
