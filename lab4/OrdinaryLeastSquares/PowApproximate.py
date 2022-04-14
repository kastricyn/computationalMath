from math import log, exp

from basic import OrdinaryLeastSquareBasicApproximation
from lineApproximation import LineApproximate


class PowApproximate(OrdinaryLeastSquareBasicApproximation):

    def __init__(self, points: list[tuple[float, float]]):
        super().__init__(points)
        self.b_ = None
        self.a_ = None

    def approximate(self):
        if not all(point[0] > 0 and point[1] > 0 for point in self.points):
            return

        lin_points = [(log(self.x[i]), log(self.y[i])) for i in range(self.n)]
        line_approximate = LineApproximate(lin_points)

        a = self.a_ = exp(line_approximate.b_)
        b = self.b_ = line_approximate.a_

        self.func = lambda x: a * (x ** b)
        self.func_str = f"{round(a, 3)}*x^{round(b, 3)}"
