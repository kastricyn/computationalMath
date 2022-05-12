import pandas as pd
from myLib.FunTwoVariable import FunTwoVariable


def EulerMethodImprove(fun: FunTwoVariable, compact: tuple[float, float], h: float, y0: float) -> list[dict]:
    a, b = compact
    ans = [{"i": 0, "x_i": a, "y_i~": "-", "f(x_i, y_i~)": "-", "y_i": y0, "f(x_i, y_i)": fun(a, y0)}]

    for i in range(1, int((b - a) / h) + 1):
        prev = ans[-1]
        dict = {"i": i, "x_i": a + i * h, "y_i~": prev["y_i"] + h * prev["f(x_i, y_i)"]}
        dict["f(x_i, y_i~)"] = fun(dict["x_i"], dict["y_i~"])
        dict["y_i"] = prev["y_i"] + h / 2 * (prev["f(x_i, y_i)"] + dict["f(x_i, y_i~)"])
        dict["f(x_i, y_i)"] = fun(dict["x_i"], dict["y_i"])
        ans.append(dict)
    return ans


def EulerMethodImproveWithEpsilon(fun: FunTwoVariable, compact: tuple[float, float], h: float, y0: float,
                                  epsilon: float = None) -> list[dict]:
    prev = EulerMethodImprove(fun, compact, h, y0)
    if epsilon is None:
        return prev
    h /= 2
    cur = EulerMethodImprove(fun, compact, h / 2, y0)
    p = 2
    while epsilon <= abs(cur[-1]["y_i"] - prev[-1]["y_i"]) / (2 ** p - 1):
        prev = cur
        h /= 2
        cur = EulerMethodImprove(fun, compact, h / 2, y0)
    return prev

