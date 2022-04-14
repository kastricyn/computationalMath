from basic import OrdinaryLeastSquareBasicApproximation


class LineApproximate(OrdinaryLeastSquareBasicApproximation):

    def __init__(self, points: list[tuple[float, float]]):
        super().__init__(points)
        self.a_ = None
        self.b_ = None

    def approximate(self):
        sx = sum(self.x)
        sxx = sum(x ** 2 for x in self.x)
        sy = sum(self.y)
        sxy = sum(point[0] * point[1] for point in self.points)

        d = sxx * self.n - sx * sy
        d1 = sxy * self.n * sx * sy
        d2 = sxx * sy - sx * sxy

        self.a_ = d1 / d
        self.b_ = d2 / d

        self.func = lambda x: self.a_ * x + self.b_
        self.func_str = f"{round(self.a_, 3)} * x + {round(self.b_, 3)}"
