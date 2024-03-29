import sys
from enum import auto

from strenum import CamelCaseStrEnum

from function import Function
from decimal import Decimal as MyDecimal

lambdas = {
    "-69*x**3/50 - 271*x**2/50 + 257*x/100 + 219/20": lambda x: MyDecimal(-69) * x ** MyDecimal(3) / MyDecimal(50) - MyDecimal(271) * x ** MyDecimal(2) / MyDecimal(50) + MyDecimal(257) * x / MyDecimal(100) + MyDecimal(219) / MyDecimal(20),
    "-x**3 + 567*x**2/100 - 178*x/25 + 67/50": lambda x: MyDecimal(-1)*x ** MyDecimal(3) + MyDecimal(567) * x ** MyDecimal(2) / MyDecimal(100) - MyDecimal(178) * x / MyDecimal(25) + MyDecimal(67) / MyDecimal(50),
    "x**2 + 20*x - 2": lambda x: x ** MyDecimal(2) + MyDecimal(20) * x - MyDecimal(2),
    "x**4 + 481*x**2/100 - 1737*x/100 + 269/50": lambda x: x ** MyDecimal(4) + MyDecimal(481) * x ** MyDecimal(2) / MyDecimal(100) - MyDecimal(1737) * x / MyDecimal(100) + MyDecimal(269) / MyDecimal(50),
    "x**3 - 189*x**2/100 - 2*x + 44/25": lambda x: x ** MyDecimal(3) - MyDecimal(189) * x ** MyDecimal(2) / MyDecimal(100) - MyDecimal(2) * x + MyDecimal(44) / MyDecimal(25),
}


def solve(fun: Function, method: str, solve_interval: tuple[float, float], epsilon: float,
          iterate_number: int = None) -> tuple[float | MyDecimal, int]:
    chosen_method = SolveMethod.get_methods().get(method)
    if chosen_method is None:
        raise SolveMethod.InvalidMethodName("No find this method")
    match chosen_method:
        case SolveMethod.chord | SolveMethod.simple_iteration:
            return chosen_method(fun, solve_interval, epsilon, iterate_number)
        case _:
            print("Check map name of method onto programm methods", file=sys.stderr)


class SolveNameMethod(CamelCaseStrEnum):
    chord = auto()
    simple_iteration = auto()


class SolveMethod:
    @staticmethod
    def chord(fun: Function, solve_interval: tuple[float | MyDecimal, float | MyDecimal], epsilon: float | MyDecimal,
              iterate_number: int = None) -> tuple[float | MyDecimal, int]:
        fun = lambdas[fun.__str__()]
        a, b = solve_interval
        a = MyDecimal(str(a))
        b = MyDecimal(str(b))

        if MyDecimal(fun(a)) * MyDecimal(fun(b)) > 0:
            raise SolveMethod.OneSignOfFunOnEndsOfCompact(
                "Выберите отрезок, на концах которого функция принимает значения с разными знаками")

        def new_x(x: MyDecimal) -> MyDecimal:
            return x - (a - x) / (fun(a) - fun(x)) * fun(x)

        x: MyDecimal = b

        if iterate_number is not None:
            for _ in range(iterate_number):
                x = new_x(x)
            return x, iterate_number

        next_x = new_x(x)
        i = 1
        while MyDecimal(epsilon) < abs(fun(x)):
            x = next_x
            next_x = new_x(x)
            i += 1
        return next_x, i

    @staticmethod
    def simple_iteration(fun: Function, solve_interval: tuple[float, float], epsilon: float, iterate_number: int,
                         trace: bool = False) -> \
            tuple[float, int]:
        l: float = -1 / fun.diff().abs().maximum(solve_interval)
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
        i = 0
        if trace:
            print("i\tx_k\tf(x_k)\tx_k+1", file=sys.stderr)
            print(f"{i}\t{x}\t{fun.subs(x)}\t{next_x}", file=sys.stderr)
        # while not end_iteration_condition(x, next_x):
        while epsilon < abs(fun.subs(next_x)):
            x = next_x
            next_x = phi.subs(x)
            i += 1
            if trace:
                print(f"{i}\t{x}\t{fun.subs(x)}\t{next_x}", file=sys.stderr)
        return next_x, i+1

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
