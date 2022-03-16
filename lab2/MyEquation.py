import sympy as sp


class MyEquation:
    def __init__(self, equation, symbols: str = "x"):
        self.symbols = sp.symbols(symbols)
        self.equation = equation

    def solve(self, method, param: set) -> map[str, float]:
        method(param)

    def substitute(self, val: float) -> float:
        # todo
        pass


