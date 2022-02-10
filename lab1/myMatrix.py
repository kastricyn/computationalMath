import math

import numpy as np


class MyMatrix:
    def __init__(self, extendMatrixArray):
        def validate(array):
            for i in array:
                if len(i) != len(array) + 1:
                    return False
            return True

        if not validate(extendMatrixArray):
            raise InvalidArrayForCreateMatrix("Can't create matrix")
        self.matrix = np.array(extendMatrixArray)  # use default parameter dtype = float64
        self.n = len(extendMatrixArray)

    def print(self):
        print(self.matrix)

    def checkDiagonalDominance(self):
        isStrongly = False
        for i in range(self.n):
            s = sum(self.matrix[i, :self.n])
            if 2 * self.matrix[i, i] < s:
                return False
            if 2 * self.matrix[i, i] > s:
                isStrongly = True
        return isStrongly

    def norma(self):
        return math.sqrt(sum((i ** 2 for i in self.matrix.flat)))


class InvalidArrayForCreateMatrix(Exception):
    pass
