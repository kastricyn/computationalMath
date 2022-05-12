import pandas as pd
from prettytable import PrettyTable

from myLib.Scanner import Scanner
from myLib.FunTwoVariable import FunTwoVariable
from count_diff import EulerMethodImproveWithEpsilon

functions = [
    "y*cos(x) + sin(x + y)", "y + (1+x)y^2",
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

    print("Усовершенствованный метод Эйлера")
    print(pd.DataFrame.from_records(EulerMethodImproveWithEpsilon(fun, (a, b), h, y0, epsilon), index="i"))

    print("Метод Адамаса")