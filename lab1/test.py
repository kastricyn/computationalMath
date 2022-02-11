import random
import unittest

import numpy as np

from myMatrix import MyMatrix


class TestCheckDiagonalDominance(unittest.TestCase):
    def test_teachExample(self):
        matrix = MyMatrix([[2, 2, 10, 0], [10, 1, 1, 0], [2, 10, 1, 0]])
        self.assertFalse(matrix.check_diagonal_dominance())
        matrix = MyMatrix([[10, 1, 1, 0], [2, 10, 1, 0], [2, 2, 10, 0]])
        self.assertTrue(matrix.check_diagonal_dominance())

    def test_Strongly(self):
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [6, 4, 10, 0]])
        self.assertFalse(matrix.check_diagonal_dominance())
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [5, 4, 10, 0]])
        self.assertTrue(matrix.check_diagonal_dominance())

    def test_sumWithoutFreeMember(self):
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [6, 4, 10, -1]])
        self.assertFalse(matrix.check_diagonal_dominance())
        matrix = MyMatrix([[10, 5, 5, 0], [5, 11, 5, 10], [5, 5, 10, 1000]])
        self.assertTrue(matrix.check_diagonal_dominance())

    def test_Float(self):
        matrix = MyMatrix([[10, 2.5, 7.5, 0], [5, 10, 5, 0], [6, 4, 10, -1]])
        self.assertFalse(matrix.check_diagonal_dominance())
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10.0001, 5.0000001, 10], [5, 5, 10, 1000]])
        self.assertTrue(matrix.check_diagonal_dominance())


class TestTryMoveEquations(unittest.TestCase):
    def test_teachExample(self):
        matrix = MyMatrix([[2, 2, 10, 14], [10, 1, 1, 12], [2, 10, 1, 13]])
        matrix.try_move_equations()
        self.assertTrue(np.array_equal(matrix.matrix, [[10, 1, 1, 12], [2, 10, 1, 13], [2, 2, 10, 14]]))


class TestCopyMyMatrix(unittest.TestCase):
    def test(self):
        matrix = MyMatrix([[10, 2.5, 7.5, 0], [5, 10, 5, 0], [6, 4, 10, -1]])
        ans = matrix.copy()
        ans.matrix[0] = 0

        self.assertIsInstance(ans, MyMatrix)
        self.assertTrue(np.array_equal(ans.matrix, [[0, 0, 0, 0], [5, 10, 5, 0], [6, 4, 10, -1]]))
        self.assertTrue(np.array_equal(matrix.matrix, [[10, 2.5, 7.5, 0], [5, 10, 5, 0], [6, 4, 10, -1]]))


class TestGetVectorColumn(unittest.TestCase):
    def test_tech(self):
        matrix = MyMatrix([[10, 1, 1, 12], [2, 10, 1, 13], [2, 2, 10, 14]])
        ans = matrix.get_vector_column_system()
        self.assertTrue(np.array_equal(ans.matrix, [[0, -0.1, -0.1, 1.2], [-.2, 0, -.1, 1.3], [-.2, -.2, 0, 1.4]]))


class TestInsertVectorIntoSystem(unittest.TestCase):

    def assertAlmostEqualList(self, first, second):
        self.assertEqual(len(second), len(first))
        for i in range(len(first)):
            self.assertAlmostEqual(first[i], second[i])

    def test_insertZero(self):
        matrix = MyMatrix([[0, -0.1, -0.1, 1.2], [-.2, 0, -.1, 1.3], [-.2, -.2, 0, 1.4]])
        first = matrix.insert_vector_into_vector_column_system([0, 0, 0])
        second = [1.2, 1.3, 1.4]
        self.assertAlmostEqualList(first, second)

    def test_insertOne(self):
        matrix = MyMatrix([[0, -0.1, -0.1, 1.2], [-.2, 0, -.1, 1.3], [-.2, -.2, 0, 1.4]])
        first = matrix.insert_vector_into_vector_column_system([1, 1, 1])
        second = [1, 1, 1]
        self.assertAlmostEqualList(first, second)

    def test_insertRandomVectorIntoEyeMatrix(self):
        for i in range(20):
            matrix = MyMatrix([])
            matrix.n = i
            matrix.matrix = np.column_stack((np.eye(i), [0] * i))
            second = [random.random() for _ in range(i)]
            first = matrix.insert_vector_into_vector_column_system(second)
            self.assertAlmostEqualList(first, second)
    def test_insertRandomVectorIntoOneMatrix(self):
        for i in range(20):
            matrix = MyMatrix([])
            matrix.n = i
            matrix.matrix = np.column_stack((np.ones((i, i)), [0] * i))
            vector = [random.random() for _ in range(i)]
            first = matrix.insert_vector_into_vector_column_system(vector)
            second = [sum(vector)]*i
            self.assertAlmostEqualList(first, second)


class TestNormaOfMatrix(unittest.TestCase):
    def test_tech(self):
        matrix = MyMatrix([[0, -0.1, -0.1, 1.2], [-.2, 0, -.1, 1.3], [-.2, -.2, 0, 1.4]])
        self.assertAlmostEqual(.3872983346207417, matrix.norma())


if __name__ == '__main__':
    unittest.main()
