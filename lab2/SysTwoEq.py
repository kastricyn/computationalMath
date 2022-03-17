import sys
from enum import auto
from strenum import CamelCaseStrEnum

from FunTwoVariable import FunTwoVariable


class SysTwoEquation:
    def __init__(self, fun1: FunTwoVariable, fun2: FunTwoVariable):
        self.fun1 = fun1
        self.fun2 = fun2

    def solve(self, point_min: tuple[float, float], point_max: tuple[float, float], epsilon: float,
              iterate_number: int = None) -> tuple[tuple[float, float], int]:
        self.fun1 -= FunTwoVariable("x")
        self.fun2 -= FunTwoVariable("y")

    def simple_iteration(fun: Function, solve_interval: tuple[float, float], epsilon: float, iterate_number: int) -> \
            tuple[float, int]:
        print(fun.diff())
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
        i = 2
        # while not end_iteration_condition(x, next_x):
        while epsilon < fun.subs(next_x):
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
