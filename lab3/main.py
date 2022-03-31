from integrate import IntegrateNameMethod, integrate
from lab3.function import Function
from myLib.Scanner import Scanner


functions = [
    "sin(x)", "cos(2x)", "x^2+20x-2", "sin(3x + pi/2)/cos(x)"
]

if __name__ == '__main__':
    print("Выберите подынтегральную функцию путём ввода номера это функции:")
    for i in range(len(functions)):
        print(f"\t{i + 1}. {functions[i]}")
    funstr = functions[int(input()) - 1]
    fun = Function(funstr)

    print("Выберите метод интегрирования:")
    for i in IntegrateNameMethod:
        print(f"\t {i}")
    method = input().strip()

    print("Введите через enter три числа: начало интервала, конец интервала и "
          "необходимую точность (кол-во знаков после запятой):")
    a = Scanner.getFloat(greeting="Начало интервала")
    b = Scanner.getFloat(greeting="Конец интервала")
    epsilon = Scanner.getInt(min=0, max=15, greeting="Необходимая точность (кол-во знаков после запятой)")
    res, n = integrate(fun, method, (a, b), 10 ** -epsilon)
    print(f"Получено значение {round(res, int(epsilon))} при разбиении на {n} интервалов")
