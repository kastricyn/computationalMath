import sys

from function import Function
from myLib.Scanner import Scanner
from solveEquation import SolveNameMethod, solve, SolveMethod

functions = [
    "-1.38x^3-5.42x^2+2.57x+10.95", "-x^3+5.67x^2-7.12x+1.34", "x^2+20x-2", "x^4+4.81x^2-17.37x+5.38",
    "x^3-1.89x^2-2x+1.76",
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

    print("Введите через enter три числа: начало интервала, конец интервала и "
          "необходимую точность (кол-во знаков после запятой):")
    # a, b, epsilon = map(float, input().split())
    a = Scanner.getFloat(greeting="Начало интервала")
    b = Scanner.getFloat(greeting="Конец интервала")
    if method == "chord":
        epsilon = Scanner.getInt(min=0, max=25, greeting="Необходимая точность (кол-во знаков после запятой)")
    else:
        epsilon = Scanner.getInt(min=0, max=15, greeting="Необходимая точность (кол-во знаков после запятой)")
    fun.plot((a, b))
    try:
        res, n = solve(fun, method, (a, b), 10 ** -epsilon)
        print(f"Получено значение корня: f({res}) = {round(fun.subs(res), epsilon + 2)} за {n} итерации")
    # except (SolveMethod.OneSignOfFunOnEndsOfCompact, TypeError):
    except SolveMethod.OneSignOfFunOnEndsOfCompact:
        print("Выберите отрезок, на концах которого функция принимает значения с разными знаками ", file=sys.stderr)
    except SolveMethod.NoConverge:
        print("Не удалось найти точку для сходимости", file=sys.stderr)
