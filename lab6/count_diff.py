import math

from myLib.FunTwoVariable import FunTwoVariable


def EulerMethodImprove(fun: FunTwoVariable, compact: tuple[float, float], h: float, y_0: float) -> list[dict]:
    a, b = compact
    ans = [{"i": 0, "x_i": a, "y_i~": "-", "f(x_i, y_i~)": "-", "y_i": y_0, "f(x_i, y_i)": fun(a, y_0)}]

    for i in range(1, int((b - a) / h) + 1):
        prev = ans[-1]
        dict = {"i": i, "x_i": a + i * h, "y_i~": prev["y_i"] + h * prev["f(x_i, y_i)"]}
        dict["f(x_i, y_i~)"] = fun(dict["x_i"], dict["y_i~"])
        dict["y_i"] = prev["y_i"] + h / 2 * (prev["f(x_i, y_i)"] + dict["f(x_i, y_i~)"])
        dict["f(x_i, y_i)"] = fun(dict["x_i"], dict["y_i"])
        ans.append(dict)
    return ans


def IterationWithEpsilon(epsilon: float = None, p=2, method=EulerMethodImprove, **kwargs) -> list[dict]:
    prev = method(**kwargs)
    if epsilon is None:
        return prev
    kwargs['h'] /= 2
    cur = method(**kwargs)
    while epsilon <= abs(cur[-1]["y_i"] - prev[-1]["y_i"]) / (2 ** p - 1):
        prev = cur
        kwargs['h'] /= 2
        cur = method(**kwargs)
    return prev


def RungeKutta(fun: FunTwoVariable, compact: tuple[float, float], h: float, y_0: float) -> list[dict]:
    a, b = compact
    ans = [{"i": 0, "x_i": a, "y_i": y_0, "f(x_i, y_i)": fun(a, y_0)}]
    for i in range(1, int((b - a) / h) + 1):
        k = [h * fun(ans[-1]["x_i"], ans[-1]["y_i"])]
        k.append(h * fun(ans[-1]["x_i"] + h / 2, ans[-1]["y_i"] + k[-1] / 2))
        k.append(h * fun(ans[-1]["x_i"] + h / 2, ans[-1]["y_i"] + k[-1] / 2))
        k.append(h * fun(ans[-1]["x_i"] + h, ans[-1]["y_i"] + k[-1]))
        dict = {"i": i, "x_i": a + i * h, "y_i": ans[-1]["y_i"] + (sum(k) + sum(k[1:3])) / 6}
        dict['f(x_i, y_i)'] = fun(dict['x_i'], dict['y_i'])
        ans.append(dict)
    return ans


def AdamsMethod(fun: FunTwoVariable, compact: tuple[float, float], h: float, y_0: float) -> list[dict]:
    a, b = compact
    ans = RungeKutta(fun, (a, a + 3.1 * h), h, y_0)
    for i in range(4, int((b - a) / h) + 1):
        f = [ans[-1]['f(x_i, y_i)']]
        f.append(ans[-1]['f(x_i, y_i)'] - ans[-2]['f(x_i, y_i)'])
        f.append(ans[-1]['f(x_i, y_i)'] - 2 * ans[-2]['f(x_i, y_i)'] + ans[-3]['f(x_i, y_i)'])
        f.append(
            ans[-1]['f(x_i, y_i)'] - 3 * ans[-2]['f(x_i, y_i)'] + 3 * ans[-3]['f(x_i, y_i)'] - ans[-4]['f(x_i, y_i)'])
        dict = {"i": i, "x_i": a + i * h}
        dict['y_i'] = ans[-1]["y_i"] + h * f[0] + 0.5 * (h ** 2) * f[1] + 5 / 12 * (h ** 3) * f[2] + 3 / 8 * (h ** 4) * \
                      f[3]
        dict['f(x_i, y_i)'] = fun(dict['x_i'], dict['y_i'])
        ans.append(dict)
    return ans
