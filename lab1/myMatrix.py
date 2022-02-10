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

    def print(self):
        print(self.matrix)


class InvalidArrayForCreateMatrix(Exception):
    pass
