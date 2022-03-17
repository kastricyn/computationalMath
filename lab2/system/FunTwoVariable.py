import sympy as sp
import matplotlib.pyplot as plt

from lab2.equation.function import Function


class FunTwoVariable:
    def __init__(self, function: str, symbols: str = "x, y"):
        self.symbols = sp.symbols(symbols)
        self.fun = sp.parse_expr(function, transformations='all')
        self.f = sp.lambdify(symbols, self.fun)

    def s(self, val: tuple[float, float]) -> float:
        x, y = val
        return self.fun.subs({"x": x, "y": y})

    def subs(self, val: tuple[float, float]) ->float:
        x, y = val
        return self.f(x, y)

    def substitute(self, val: dict[str, float]):
        return self.fun.subs(val)

    def __add__(self, other):
        return FunTwoVariable((self.fun + other.fun).__str__())

    def __sub__(self, other):
        return FunTwoVariable((self.fun - other.fun).__str__())

    def __mul__(self, other):
        return FunTwoVariable((self.fun * other.fun).__str__())

    def __truediv__(self, other):
        return FunTwoVariable((self.fun / other.fun).__str__())

    def abs(self):
        return FunTwoVariable("abs(" + self.fun.__str__() + ")")

    def diff(self):
        return FunTwoVariable(sp.diff(self.fun, self.symbols).__str__())

    def dx(self):
        return FunTwoVariable(sp.diff(self.fun.subs({"y": 1}), sp.Symbol("x")).__str__())

    def dy(self):
        return FunTwoVariable(sp.diff(self.fun.subs({"x": 1}), sp.Symbol("y")).__str__())

    def maximumAbsOfDiff(self, point_min: tuple[float, float], point_max: tuple[float, float]) -> float:
        return (self.dy().abs() + self.dx().abs()).maximum(point_min, point_max)

    def maximum(self, point_min: tuple[float, float], point_max: tuple[float, float]) -> float:
        x_min, y_min = point_min
        x_max, y_max = point_max
        interval = (x_min, x_max)
        ans = self.subs((x_min, y_min))
        for y in range(int(100 * y_min), int(100* y_max)):
            t = Function(self.substitute({"y": y/100}).__str__()).maximum(interval)
            if t > ans:
                ans = t
        return ans

    def minimum(self, point_min: tuple[float, float], point_max: tuple[float, float]) -> float:
        x_min, y_min = point_min
        x_max, y_max = point_max
        interval = sp.Interval(x_min, x_max)
        ans = self.subs((x_min, y_min))
        for y in range(int(100 * y_min), int(10 ** y_max)):
            t = sp.minimum(self.fun.subs(y / 100), sp.Symbol("x"), interval)
            if t < ans:
                ans = t
        return ans

    def print(self):
        # sp.init_printing(use_unicode=True)
        print(sp.pretty(self.fun))

    # def plot(self, compact: tuple[float, float]):
    #     start, stop = compact
    #     ax = plt.gca()
    #     # plot X - axis
    #     ax.axhline(y=0, color='c')
    #     # plot Y - axis
    #     # ax.axvline(x=0, color='g')
    #
    #     plt.plot([i / 100 for i in range(int(100 * start), int(100 * stop))],
    #              [self.f(i / 100) for i in range(int(100 * start), int(100 * stop))], color='g')
    #     plt.show()

    def __str__(self) -> str:
        return self.fun.__str__()


if __name__ == '__main__':
    f = FunTwoVariable("x^2-31+y^3").diff()
    f.print()
    print(f + FunTwoVariable("2x-35"))
    print(f * FunTwoVariable("l") + FunTwoVariable("1"))
