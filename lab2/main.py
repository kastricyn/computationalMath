from function import Function
from solveEquation import SolveNameMethod, solve

functions = [
    "sin(x)-1", "cos(2x)+2", "x^2+20x-2", "sin(3x + pi/2)/cos(x)"
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
    res, n = solve(fun, method, (a, b), 10 ** -epsilon)
    res = round(res, int(epsilon))
    print(f"Получено значение корня: f({res}) = {fun.subs({'x': res})} на {n} итерации")
