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

    def check_diagonal_dominance(self):
        is_strongly = False
        for i in range(self.n):
            s = sum(self.matrix[i, :self.n])
            if 2 * self.matrix[i, i] < s:
                return False
            if 2 * self.matrix[i, i] > s:
                is_strongly = True
        return is_strongly

    def try_move_equations(self):
        def id_of_max_element(mass):
            ans = 0
            for i in range(len(mass) - 1):
                if mass[ans] < mass[i]:
                    ans = i
            return ans

        dict = {}
        for row in self.matrix:
            dict[id_of_max_element(row)] = row
        if len(dict) == self.n:
            ans = []
            for i in range(self.n):
                ans.append(dict[i])
            self.matrix = np.array(ans)

    def norma(self):
        return math.sqrt(sum((i ** 2 for i in self.matrix.flat)))


class InvalidArrayForCreateMatrix(Exception):
    pass
