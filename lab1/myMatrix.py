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
        self.matrix = np.array(extendMatrixArray, dtype=float)
        self.n = len(extendMatrixArray)

    def print(self) -> None:
        print(self.matrix)

    def check_diagonal_dominance(self) -> bool:
        is_strongly = False
        for i in range(self.n):
            s = sum(self.matrix[i, :self.n])
            if 2 * self.matrix[i, i] < s:
                return False
            if 2 * self.matrix[i, i] > s:
                is_strongly = True
        return is_strongly

    def try_move_equations(self) -> None:
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

    def get_vector_column_system(self):  # -> MyMatrix
        ans = self.copy()
        for i in range(ans.n):
            for j in range(ans.n):
                if i == j:
                    ans.matrix[i, j] = 0
                else:
                    ans.matrix[i, j] = - self.matrix[i, j] / self.matrix[i, i]
            ans.matrix[i, ans.n] = self.matrix[i, self.n] / self.matrix[i, i]
        return ans

    def insert_vector_into_vector_column_system(self, v: list[float]) -> list[float]:
        v.append(1)
        ans = []
        for i in range(self.n):
            ans.append(sum([
                self.matrix[i, j] * v[j] for j in range(len(v))
            ]))
        v.pop()
        return ans

    def norma(self) -> float:
        return math.sqrt(sum((i ** 2 for i in self.matrix[:, :self.n].flat)))

    def copy(self):
        return MyMatrix(self.matrix.copy())


class InvalidArrayForCreateMatrix(Exception):
    pass
