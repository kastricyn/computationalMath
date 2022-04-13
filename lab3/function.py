import sympy as sp


class Function:
    def __init__(self, function: str, symbols: str = "x"):
        self.symbols = sp.Symbol(symbols)
        self.fun = sp.parse_expr(function, transformations='all')
        self.f = sp.lambdify(symbols, self.fun)

    def subs(self, val: dict[str, float]) -> float:
        # return self.fun.subs(val)
        return self.f(val['x'])

    def __str__(self) -> str:
        return self.fun.__str__()
