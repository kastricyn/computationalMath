from function import Function
from integrate import IntegrateNameMethod, integrate

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

    print("Введите через пробел три числа: начало интервала интегрирования, конец интервала интегрирования и "
          "необходимую точность (кол-во знаков после запятой):")
    a, b, epsilon = map(float, input().split())
    res, n = integrate(fun, method, (a, b), 10 ** -epsilon)
    print(f"Получено значение {round(res, int(epsilon))} при разбиении на {n} интервалов")
