import unittest

from myMatrix import MyMatrix


class TestCheckDiagonalDominance(unittest.TestCase):
    def test_teachExample(self):
        matrix = MyMatrix([[2, 2, 10, 0], [10, 1, 1, 0], [2, 10, 1, 0]])
        self.assertFalse(matrix.checkDiagonalDominance())
        matrix = MyMatrix([[10, 1, 1, 0], [2, 10, 1, 0], [2, 2, 10, 0]])
        self.assertTrue(matrix.checkDiagonalDominance())

    def test_Strongly(self):
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [6, 4, 10, 0]])
        self.assertFalse(matrix.checkDiagonalDominance())
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [5, 4, 10, 0]])
        self.assertTrue(matrix.checkDiagonalDominance())

    def test_sumWithoutFreeMember(self):
        matrix = MyMatrix([[10, 5, 5, 0], [5, 10, 5, 0], [6, 4, 10, -1]])
        self.assertFalse(matrix.checkDiagonalDominance())
        matrix = MyMatrix([[10, 5, 5, 0], [5, 11, 5, 10], [5, 5, 10, 1000]])
        self.assertTrue(matrix.checkDiagonalDominance())


if __name__ == '__main__':
    unittest.main()
