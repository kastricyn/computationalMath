import sympy as sp
import matplotlib.pyplot as plt


class Function:
    def __init__(self, function: str, symbols: str = "x"):
        self.symbols = sp.Symbol(symbols)
        self.fun = sp.parse_expr(function, transformations='all')
        self.f = sp.lambdify(symbols, self.fun)

    def subs(self, val) -> float:
        return self.fun.subs({"x": val})

    def s(self, val) -> float:
        return self.f(val)

    def __add__(self, other):
        return Function((self.fun + other.fun).__str__())

    def __sub__(self, other):
        return Function((self.fun - other.fun).__str__())

    def __mul__(self, other):
        return Function((self.fun * other.fun).__str__())

    def __truediv__(self, other):
        return Function((self.fun / other.fun).__str__())

    def abs(self):
        return Function("abs(" + self.fun.__str__() + ")")

    def diff(self):
        return Function(sp.diff(self.fun, self.symbols).__str__())

    def maximum(self, compact: tuple[float, float], step_number: int = 100) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        try:
            return sp.maximum(self.fun, self.symbols, interval)
        except NotImplementedError:
            ans = self.s(a)
            for i in range(int(step_number * a), int(step_number * b) + 1):
                t = self.s(i / step_number)
                if ans < t:
                    ans = t
            return ans

    def minimum(self, compact: tuple[float, float], step_number: int = 100) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        try:
            return sp.minimum(self.fun, self.symbols, interval)
        except NotImplementedError:
            ans = self.s(a)
            for i in range(int(step_number * a), int(step_number * b) + 1):
                t = self.s(i / step_number)
                if ans > t:
                    ans = t
            return ans

    def print(self):
        # sp.init_printing(use_unicode=True)
        print(sp.pretty(self.fun))

    def plt(self, compact: tuple[float, float]):
        sp.plotting.plot(self.fun, line_color='red')
        x = sp.Symbol("x")
        sp.plot((sp.sin(x), (x, -sp.pi, sp.pi)), line_color='red', title='Пример графика SymPy')

    def plot(self, compact: tuple[float, float]):
        start, stop = compact
        ax = plt.gca()
        # plot X - axis
        ax.axhline(y=0, color='c')
        # plot Y - axis
        # ax.axvline(x=0, color='g')

        plt.plot([i / 100 for i in range(int(100 * start), int(100 * stop))],
                 [self.f(i / 100) for i in range(int(100 * start), int(100 * stop))], color='r')
        plt.show()

    def __str__(self) -> str:
        return self.fun.__str__()


if __name__ == '__main__':
    f = Function("abs(x^2-31)")
    f.print()
    print(f + Function("2x-35"))
    print(f * Function("l") + Function("1"))
    print(f.maximum((0, 3)))
    print(f.minimum((0, 7)))
