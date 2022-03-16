import sympy as sp


class Function:
    def __init__(self, function: str):
        self.fun = sp.parse_expr(function, transformations='all')
        # self.f = sp.Lambda(function)

    def subs(self, val: dict[str, float]) -> float:
        return self.fun.subs(val)
        # return self.f(val[0])

    def __str__(self) -> str:
        return self.fun.__str__()
