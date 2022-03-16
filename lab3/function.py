import sympy as sp


class Function:
    def __init__(self, function: str):
        self.fun = sp.parse_expr(function, transformations='all')

    def subs(self, val: dict[str, float]) -> float:
        return self.fun.subs(val)

    def __str__(self) -> str:
        return self.fun.__str__()
