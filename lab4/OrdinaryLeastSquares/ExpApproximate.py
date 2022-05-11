from math import log, exp

from lab4.OrdinaryLeastSquares.OLSbasic import OrdinaryLeastSquareBasicApproximation
from lab4.OrdinaryLeastSquares.PolinomApproximation import PolinomApproximate


class ExpApproximate(OrdinaryLeastSquareBasicApproximation):

    def __init__(self, points: list[tuple[float, float]]):
        super().__init__(points)

    def approximate(self):
        if not all(point[1] > 0 for point in self.points):
            return

        lin_points = [(self.x[i], log(self.y[i])) for i in range(self.n)]
        line_approximate = PolinomApproximate(lin_points)

        a  = exp(line_approximate.b_)
        b  = line_approximate.a_

        self.func = lambda x: a * exp(x * b)
        self.func_str = f"{round(a, 3)} * e^({round(b, 3)}x)"
