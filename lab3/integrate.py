import sys
from enum import auto
from strenum import CamelCaseStrEnum

from function import Function


def integrate(fun: Function, method: str, integrate_interval: tuple[float, float], epsilon: float,
              compact_number: int = None) -> tuple[float, int]:
    chosen_method = IntegrateMethod.get_methods().get(method)
    if chosen_method is None:
        raise IntegrateMethod.InvalidMethodName("No find this method")
    match chosen_method:
        case IntegrateMethod.left_rectangle | IntegrateMethod.center_rectangle | IntegrateMethod.right_rectangle \
             | IntegrateMethod.trapeze:
            return IntegrateMethod.abstract_method(fun, chosen_method, integrate_interval, epsilon,
                                                   compact_number=compact_number)
        case IntegrateMethod.simpson:
            return IntegrateMethod.abstract_method(fun, chosen_method, integrate_interval, epsilon,
                                                   runge_denominator=15, compact_number=compact_number)
        case _:
            print("Check map name of method onto programm methods", file=sys.stderr)


class IntegrateNameMethod(CamelCaseStrEnum):
    leftRectangular = auto()
    centerRectangular = auto()
    rightRectangular = auto()
    trapeze = auto()


class IntegrateMethod:
    @staticmethod
    def abstract_method(fun: Function, integrate_sum, integrate_interval: tuple[float, float],
                        epsilon: float, runge_denominator: int = 3, compact_number: int = None) -> tuple[float, int]:
        if compact_number is None:
            compact_number: int = 4
        else:
            return integrate_sum(fun, integrate_interval, compact_number), compact_number
        integral: float = integrate_sum(fun, integrate_interval, compact_number)
        while True:
            second_integral: float = integrate_sum(fun, integrate_interval, compact_number * 2)
            if abs(integral - second_integral) / runge_denominator < abs(epsilon):
                return second_integral, compact_number * 2
            integral = second_integral
            compact_number *= 2

    @staticmethod
    def left_rectangle(fun: Function, integrate_interval: tuple[float, float], compact_number: int) -> float:
        a, b = integrate_interval
        size_of_compact = IntegrateMethod.__size_of_compact__(integrate_interval, compact_number)
        return sum(
            fun.subs({"x": a + i * size_of_compact}) * size_of_compact
            for i in range(compact_number))

    @staticmethod
    def center_rectangle(fun: Function, integrate_interval: tuple[float, float], compact_number: int) -> float:
        a, b = integrate_interval
        size_of_compact = IntegrateMethod.__size_of_compact__(integrate_interval, compact_number)
        return sum(
            fun.subs({"x": a + (i + 0.5) * size_of_compact}) * size_of_compact
            for i in range(compact_number))

    @staticmethod
    def right_rectangle(fun: Function, integrate_interval: tuple[float, float], compact_number: int) -> float:
        a, b = integrate_interval
        size_of_compact = IntegrateMethod.__size_of_compact__(integrate_interval, compact_number)
        return sum(
            fun.subs({"x": a + (i + 1) * size_of_compact}) * size_of_compact
            for i in range(compact_number))

    @staticmethod
    def trapeze(fun: Function, integrate_interval: tuple[float, float], compact_number: int) -> float:
        a, b = integrate_interval
        size_of_compact = IntegrateMethod.__size_of_compact__(integrate_interval, compact_number)
        return sum(
            0.5 * (fun.subs({"x": a + i * size_of_compact}) + fun.subs(
                {"x": a + (i + 1) * size_of_compact})) * size_of_compact
            for i in range(compact_number))

    @staticmethod
    def simpson():
        pass

    @staticmethod
    def __size_of_compact__(integrate_interval: tuple[float, float], compact_number: int) -> float:
        a, b = integrate_interval
        return (b - a) / compact_number

    @staticmethod
    def get_methods() -> dict:
        return {
            IntegrateNameMethod.leftRectangular: IntegrateMethod.left_rectangle,
            IntegrateNameMethod.centerRectangular: IntegrateMethod.center_rectangle,
            IntegrateNameMethod.rightRectangular: IntegrateMethod.right_rectangle,
            IntegrateNameMethod.trapeze: IntegrateMethod.trapeze,
        }

    class InvalidMethodName(Exception):
        pass
