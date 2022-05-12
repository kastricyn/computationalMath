import pandas as pd
import matplotlib.pyplot as plt

from myLib.Scanner import Scanner
from myLib.FunTwoVariable import FunTwoVariable
from count_diff import IterationWithEpsilon, EulerMethodImprove, RungeKutta, AdamsMethod

functions = [
    "y + (1+x)y^2",
]

if __name__ == '__main__':
    print("Выберите уравнение путём ввода его номера:")
    for i in range(len(functions)):
        print(f"\t{i + 1}. y' = {functions[i]}")
        # print(FunTwoVariable(functions[i])) # just print beautiful view of functions
    funstr = functions[int(input()) - 1]
    fun = FunTwoVariable(funstr)

    print("Введите через enter 5 чисел: начало интервала (a), конец интервала (b), начальное условие (y(a)), шаг (h) и "
          "необходимую точность (кол-во знаков после запятой):")
    x0 = a = Scanner.getFloat(greeting="Начало интервала (a)")
    b = Scanner.getFloat(greeting="Конец интервала (b)")
    y0 = Scanner.getFloat(greeting="Начальное условие y(a)")
    h = Scanner.getFloat(greeting="Шаг (h)")
    epsilon = 10 ** -Scanner.getInt(min=0, max=15, greeting="Необходимая точность (кол-во знаков после запятой)")

    print(
        f"Решаем уравнение y' = {funstr} с начальным условием y({x0}) = {y0}, выбрав шаг h = {h} на отрезке [{a}, {b}]:")

    print("\nУсовершенствованный метод Эйлера")
    euler_pro = pd.DataFrame.from_records(
        IterationWithEpsilon(epsilon, p=2, method=EulerMethodImprove, fun=fun, compact=(a, b), h=h, y_0=y0), index="i")
    print(euler_pro)

    print("\nМетод Рунге-Кутта 4- го порядка")
    rk = pd.DataFrame.from_records(
        IterationWithEpsilon(epsilon, p=4, method=RungeKutta, fun=fun, compact=(a, b), h=h, y_0=y0), index="i")
    print(rk)

    print("\nМетод Адамса")
    adams = pd.DataFrame.from_records(
        IterationWithEpsilon(epsilon, p=4, method=AdamsMethod, fun=fun, compact=(a, b), h=h, y_0=y0), index="i")
    print(adams)

    ideals = [[1, 1.1, 1.2, 1.3, 1.4, 1.5],[-1, -0.909091, -0.833333, -0.769231, -0.714286, -0.666667]]

    plt.grid()
    plt.scatter(adams["x_i"], adams["y_i"], c='g', s=5, label="Метод Адамса")
    plt.scatter(euler_pro["x_i"], euler_pro["y_i"], c='r', s=5, label="Усовершенствованный метод Эйлера")
    plt.scatter(rk["x_i"], rk["y_i"], c='b', s=5, label="Метод Рунге-Кутта 4-го порядка")
    plt.scatter(ideals[0], ideals[1], c='k', s=5, label="Точный метод")
    plt.legend()
    plt.show()
