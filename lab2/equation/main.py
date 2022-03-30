import sys

from function import Function
from solveEquation import SolveNameMethod, solve, SolveMethod

functions = [
    "2sin(x)-1", "sin(2x)-1/2", "x^2+20x-2", "cos(3x + pi/2)/sin(x)"
]

if __name__ == '__main__':
    print("Выберите уравнение путём ввода его номера:")
    for i in range(len(functions)):
        print(f"\t{i + 1}. {functions[i]} = 0")
    funstr = functions[int(input()) - 1]
    fun = Function(funstr)

    print("Выберите метод решения:")
    for i in SolveNameMethod:
        print(f"\t {i}")
    method = input().strip()

    print("Введите через пробел три числа: начало интервала, конец интервала и "
          "необходимую точность (кол-во знаков после запятой):")
    a, b, epsilon = map(float, input().split())
    fun.plot((a, b))
    try:
        res, n = solve(fun, method, (a, b), 10 ** -epsilon)
        res = round(res, int(epsilon))
        print(f"Получено значение корня: f({res}) = {fun.subs(res)} за {n} итерации")
    except SolveMethod.OneSignOfFunOnEndsOfCompact:
        print("Выберите отрезок, на концах которого функция принимает значения с разными знаками", file=sys.stderr)
    except SolveMethod.NoConverge:
        print("Не удалось найти точку для сходимости", file=sys.stderr)
