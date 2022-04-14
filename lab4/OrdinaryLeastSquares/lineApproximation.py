from basic import OrdinaryLeastSquareBasicApproximation


class lineApproximate(OrdinaryLeastSquareBasicApproximation):
    def updateResultY(self):
        self.resultY = [self.func(i) for i in self.x]

    def approximation_line(self):
        sx = sum(self.x)
        sxx = sum(x**2 for x in self.x)
        sy = sum(self.y)
        sxy = sum(point[0]*point[1] for point in self.points)

        d = sxx*self.n-sx*sy
