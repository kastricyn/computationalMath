from enum import auto
from strenum import CamelCaseStrEnum

from function import Function


def solve(fun: Function, method: str, solve_interavl: tuple[float, float], epsilon: float,
          iterate_number: int = None) -> tuple[float, int]:
    chosen_method = SolveMethod.get_methods().get(method)
    if chosen_method is None:
        raise SolveMethod.InvalidMethodName("No find this method")
    match chosen_method:
        case SolveNameMethod.chord:
            return SolveMethod.chord(fun, solve_interavl, epsilon, iterate_number)


class SolveNameMethod(CamelCaseStrEnum):
    chord = auto()
    simple_iteration = auto()


class SolveMethod:
    @staticmethod
    def chord(fun: Function, solve_interval: tuple[float, float], epsilon: float, iterate_number: int = None) -> \
            tuple[float, int]:
        a, b = solve_interval
        if fun.subs({"x": a}) * fun.subs({"x": b}) > 0:
            raise SolveMethod.OneSignOfFunOnEndsOfCompact(
                "Выберите отрезок, на концах которого функция принимает значения с разными знаками")

        new_x = lambda x: x - (a - x) / (fun.subs(x) - fun.subs(x)) * fun.subs(x)
        x = b

        if iterate_number is not None:
            for _ in range(iterate_number):
                x = new_x(x)
            return x, iterate_number

        next_x = new_x(x)
        i = 1
        while abs(x - next_x) > epsilon:
            x = next_x
            next_x = new_x(x)
            i += 1
        return next_x, i

    @staticmethod
    def simple_iteration(fun: Function, solve_interval: tuple[float, float], epsilon: float, iterate_number: int) -> \
            tuple[float, int]:
        l: float = -1 / fun.diff().maximum(solve_interval)
        phi = Function("x") + Function(str(l)) * fun
        q = phi.diff().abs().maximum(solve_interval)

        if iterate_number is not None:
            x = solve_interval[0]
            for _ in range(iterate_number):
                x = phi(x)
            return x, iterate_number

        if q >= 1:
            raise SolveMethod.NoConverge("Не удалось найти точку для сходимости")
        end_iteration_condition = lambda x, next_x: abs(x - next_x) <= epsilon if q <= 0.5 else abs(x - next_x) <= (
                1 - q) / q * epsilon

        x = solve_interval[0]
        next_x = phi.subs(x)
        i = 2
        while not end_iteration_condition(x, next_x):
            x = next_x
            next_x = phi.subs(x)
            i += 1
        return next_x, i

    @staticmethod
    def get_methods() -> dict:
        return {
            SolveNameMethod.chord: SolveMethod.chord,
            SolveNameMethod.simple_iteration: SolveMethod.simple_iteration,
        }

    class InvalidMethodName(Exception):
        pass

    class OneSignOfFunOnEndsOfCompact(Exception):
        pass

    class NoConverge(Exception):
        pass
