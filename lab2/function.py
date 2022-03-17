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

    def diff(self):
        return Function(sp.diff(self.fun, self.symbols).__str__())

    def maximum(self, compact: tuple[float, float]) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        return sp.maximum(self.fun, self.symbols, interval)

    def minimum(self, compact: tuple[float, float]) -> float:
        a, b = compact
        interval = sp.Interval(a, b)
        return sp.minimum(self.fun, self.symbols, interval)

    def print(self):
        # sp.init_printing(use_unicode=True)
        print(sp.pretty(self.fun))

    def __str__(self) -> str:
        return self.fun.__str__()


if __name__ == '__main__':
    f = Function("sin(x)")
    f.print()
    print(f.maximum((0, 3)))
    print(f.minimum((0, 3)))
