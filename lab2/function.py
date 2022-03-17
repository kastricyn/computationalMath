import sympy as sp


class Function:
    def __init__(self, function: str, symbols: str = "x"):
        self.symbols = sp.Symbol(symbols)
        self.fun = sp.parse_expr(function, transformations='all')
        self.f = sp.lambdify(symbols, self.fun)

    def subs(self, val: dict[str, float]) -> float:
        return self.fun.subs(val)

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
        return Function("abs(" + self.fun.__str__ + ")")

    def diff(self):
        return Function(sp.diff(self.fun, self.symbols).__str__())

    def maximum(self, compact: tuple[float, float]) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        try:
            return sp.maximum(self.fun, self.symbols, interval)
        except NotImplementedError:
            ans = self.s(a)
            for i in range(100 * a, 100 * b + 1):
                t = self.s(i / 100)
                if ans < t:
                    ans = t
            return ans

    def minimum(self, compact: tuple[float, float]) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        try:
            return sp.minimum(self.fun, self.symbols, interval)
        except NotImplementedError:
            ans = self.s(a)
            for i in range(100 * a, 100 * b + 1):
                t = self.s(i / 100)
                if ans > t:
                    ans = t
            return ans

    def print(self):
        # sp.init_printing(use_unicode=True)
        print(sp.pretty(self.fun))

    def __str__(self) -> str:
        return self.fun.__str__()


if __name__ == '__main__':
    f = Function("abs(x^2-31)")
    f.print()
    print(f + Function("2x-35"))
    print(f * Function("l") + Function("1"))
    print(f.maximum((0, 3)))
    print(f.minimum((0, 7)))
