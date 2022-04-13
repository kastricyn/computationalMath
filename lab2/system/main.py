import sys

from FunTwoVariable import FunTwoVariable
from SysTwoEq import SysTwoEquation
from myLib.Scanner import Scanner

if __name__ == '__main__':
    fun1 = FunTwoVariable("0.1x^2 - x + 0.2y^2 - 0.3")
    fun2 = FunTwoVariable("0.2x^2 - y - 0.1x*y - 0.7")
    system = SysTwoEquation(fun1, fun2)

    print("Решаем систему из ур-ний:")
    print("\t", fun1, "= 0")
    print("\t", fun2, "= 0")

    print(
        "Введите через пробел четыре числа: координаты левого нижней точки прямоугольной области (x, y) и верхнего правого")
    x_min = Scanner.getFloat(greeting="Координата x левого нижнего угла")
    y_min = Scanner.getFloat(greeting="Координата y левого нижнего угла")
    x_max = Scanner.getFloat(greeting="Координата x правого верхнего угла")
    y_max = Scanner.getFloat(greeting="Координата y правого верхнего угла")
    epsilon = Scanner.getInt(min=0, max=15, greeting="Необходимая точность (кол-во знаков после запятой)")
    try:
        system.plot((x_min, x_max), (y_min, y_max))
        res, n = system.solve((x_min, y_min), (x_max, y_max), 10 ** -epsilon)
        x, y = res
        x = round(x, epsilon)
        y = round(y, epsilon)
        print(f"Получено значение корня: ({x}, {y}) :\n",
              f"fun1({x}, {y}) = {fun1.subs((x, y))} \n",
              f"fun2({x}, {y}) = {fun2.subs((x, y))} \n",
              f" за {n} итерации")
    except SysTwoEquation.ConditionConvergeFalse:
        print("условие сходимости не выполнено", file=sys.stderr)
