from math import sqrt

from metrics import Metrix


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

        self._polinom_degree = 2
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

    def updateResultY(self):
        self.resultY = [self.func(i) for i in self.x]

    def __str__(self):
        return self.func_str
