# Game of life
# no parallelization


import Define
import numpy as np


def gameoflife(matrix):
    # increase neighbours

    neighbours = np.zeros([Define.M, Define.N], int)
    for m in range(Define.M):
        for n in range(Define.N):
            if matrix[m, n]:  # if is one update surrounding fields
                if m == 0:  # oben
                    if n == 0:  # oben links
                        updateFields(neighbours, m, m+1, n, n+1, m, n)
                    elif n == Define.N-1:  # oben rechts
                        updateFields(neighbours, m, m+1, n-1, n, m, n)
                    else:
                        updateFields(neighbours, m, m+1, n-1, n+1, m, n)
                elif m == Define.M-1:  # unten
                    if n == 0:  # unten links
                        updateFields(neighbours, m-1, m, n, n+1, m, n)
                    elif n == Define.N-1:  # unten rechts
                        updateFields(neighbours, m-1, m, n-1, n, m, n)
                    else:
                        updateFields(neighbours, m-1, m, n-1, n+1, m, n)
                else:   # mitte
                    if n == 0:
                        updateFields(neighbours, m-1, m+1, n, n+1, m, n)
                    elif n == Define.N-1:  # oben rechts
                        updateFields(neighbours, m-1, m+1, n-1, n, m, n)
                    else:
                        updateFields(neighbours, m-1, m+1, n-1, n+1, m, n)
    # print "neighbour matrix"
    print neighbours

    # set new values in matrix accourding to rules
    for m in range(Define.M):
        for n in range(Define.N):
            num = neighbours[m, n]
            if num < 2 or num > 3:
                matrix[m, n] = 0
            else:
                if matrix[m, n] != 1 and num == 2:
                    matrix[m, n] = 0
                else:
                    matrix[m, n] = 1



def updateFields(neighbours, oben, unten, links, rechts, y, x):
#   print "oben: ", oben
#   print "unten: ", unten
#   print "links: ", links
#   print "rechts:", rechts
#   print "x ", x
#   print "y ", y
    for i in range(oben, unten+1):
#        print i
        for j in range(links, rechts+1):
#            print j
            if not(x == j and y == i):
                neighbours[i, j] += 1
