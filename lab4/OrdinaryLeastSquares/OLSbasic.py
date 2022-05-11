from math import sqrt

class OrdinaryLeastSquareBasicApproximation:

    def __init__(self, points: list[tuple[float, float]]):
        self.points = points
        self.x = [point[0] for point in points]
        self.y = [point[1] for point in points]
        self.n = len(points)
        self.func = None
        self.func_str: str | None = None
        self.resultY: list[float] | None = None
        self.metrix: dict[str, float] = dict()
        self._polinom_degree = 1
        self.approximate()
        self.updateResultY()
        self.count_metrix()

    def approximate(self):
        '''
        Must be overridden for certain method
        :return: None,
        but change self.func, self.func_str
        '''
        pass

    def count_metrix(self):
        self.metrix['S'] = sum([
            (self.resultY[i] - self.y[i]) ** 2 for i in range(self.n)
        ])
        self.metrix["sigma"] = sqrt(self.metrix["S"] / self.n)
        pass

    def coeff_pirsona(self):
        x = self.x
        y = self.y
        n = self.n
        x_average = sum(x) / n
        y_average = sum(y) / n
        self.metrix['pirson'] = sum([(x[i] - x_average) * (y[i] - y_average) for i in range(n)]) / sqrt(
            sum([(x[i] - x_average) ** 2 for i in range(n)]) * sum([(y[i] - y_average) ** 2 for i in range(n)])
        )

    def updateResultY(self):
        self.resultY = [self.func(i) for i in self.x]

    def __str__(self):
        return self.func_str
