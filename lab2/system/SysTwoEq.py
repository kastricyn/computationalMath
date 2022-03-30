import matplotlib.pyplot as plt
import numpy as np

from lab2.system.FunTwoVariable import FunTwoVariable


class SysTwoEquation:
    def __init__(self, fun1: FunTwoVariable, fun2: FunTwoVariable):
        self.fun1: FunTwoVariable = fun1
        self.fun2: FunTwoVariable = fun2

    def plot(self, x_compact: tuple[float, float], y_compact: tuple[float, float]) -> None:
        x = np.linspace(x_compact[0], x_compact[1], 100)
        y = np.linspace(y_compact[0], y_compact[1], 100)
        X, Y = np.meshgrid(x, y)
        Z1 = self.fun1.subs((X, Y))
        Z2 = self.fun2.subs((X, Y))
        plt.contour(X, Y, Z1, [0], colors=['red'])
        plt.contour(X, Y, Z2, [0], colors=['blue'])
        plt.show()

    def solve(self, point_min: tuple[float, float], point_max: tuple[float, float], epsilon: float,
              point_start: tuple[float, float] = None, iterate_number: int = None) -> tuple[
        tuple[float, float], int]:
        phi_x = self.fun1 + FunTwoVariable("x")
        phi_y = self.fun2 + FunTwoVariable("y")

        q = max(phi_x.maximumAbsOfDiff(point_min, point_max), phi_y.maximumAbsOfDiff(point_min, point_max))

        if q >= 1:
            raise SysTwoEquation.ConditionConvergeFalse("условие сходимости не выполнено")

        if point_start is None:
            point_start = point_min

        if iterate_number is not None:
            point = point_start
            for _ in range(iterate_number):
                point = phi_x.subs(point), phi_y.subs(point)
            return point, iterate_number

        point = point_start
        point_next = phi_x.subs(point), phi_y.subs(point)
        i = 1
        while epsilon < max(abs(point[0] - point_next[0]), abs(point[1] - point_next[1])):
            point = point_next
            point_next = phi_x.subs(point), phi_y.subs(point)
            i += 1
        return point_next, i

    class ConditionConvergeFalse(Exception):
        pass
