from basic import OrdinaryLeastSquareBasicApproximation


class SquareApproximate(OrdinaryLeastSquareBasicApproximation):

    def approximate(self):
        sx = sum(self.x)
        sxx = sum(x ** 2 for x in self.x)
        sy = sum(self.y)
        sxy = sum(point[0] * point[1] for point in self.points)

        d = sxx * self.n - sx * sy
        d1 = sxy * self.n * sx * sy
        d2 = sxx * sy - sx * sxy

        a = d1 / d
        b = d2 / d

        self.func = lambda x: a * x + b
        self.func_str = f"{round(a, 3)} * x + {round(b, 3)}"
