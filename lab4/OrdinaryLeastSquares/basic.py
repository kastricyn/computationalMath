class OrdinaryLeastSquareBasicApproximation:
    def __init__(self, points: list[tuple[float, float]]):
        self.points = points
        self.x = (point[0] for point in points)
        self.y = (point[1] for point in points)
        self.n = len(points)


