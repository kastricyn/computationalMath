from basic import OrdinaryLeastSquareBasicApproximation
from numpy.polynomial import Polynomial as P
from numpy.linalg import solve


class PolinomApproximate(OrdinaryLeastSquareBasicApproximation):
    def __init__(self, points: list[tuple[float, float]], polinom_degree: int = 2):
        super().__init__(points)
        self._polinom_degree = polinom_degree

    def approximate(self):
        n = self._polinom_degree  # степень полинома
        sum_pows = [sum([point[0] ** i for point in self.points]) for i in range(n * 2 + 1)]
        A = [sum_pows[i:i + n + 1] for i in range(n + 1)]

        B = [sum([point[1] * (point[0] ** i) for point in self.points]) for i in range(n + 1)]

        self.func = P(solve(A, B))
        self.func_str = self.func.__str__()


if __name__ == '__main__':
    example_line_points = [(1.2, 7.4),
                           (2.9, 9.5),
                           (4.1, 11.1),
                           (5.5, 12.9),
                           (6.7, 14.6),
                           (7.8, 17.3),
                           (9.2, 18.2),
                           (10.3, 20.7), ]
    example_square_points = [(1.1, 3.5),
                             (2.3, 4.1),
                             (3.7, 5.2),
                             (4.5, 6.9),
                             (5.4, 8.3),
                             (6.8, 14.8),
                             (7.5, 21.2), ]

    approx = PolinomApproximate(example_line_points, 1)
    approx.approximate()
    print(approx)
    print([round(_, 3) for _ in approx.resultY])
    print((approx.metrix))
