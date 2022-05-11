from myLib.FunTwoVariable import FunTwoVariable

functions = [
    "sin(x+y)+y*cos(x)"
]

if __name__ == '__main__':
    x0, y0 = map(float, input().split())
    fun = FunTwoVariable("sin(x+y)+y*cos(x)")


if __name__ == '__main__':
    print("Выберите уравнение путём ввода его номера:")
    for i in range(len(functions)):
        print(f"\t{i + 1}. {functions[i]} = 0")
    funstr = functions[int(input()) - 1]
    fun = Function(funstr)

    print("Введите через enter четыре числа: начало интервала, конец интервала и "
          "необходимую точность (кол-во знаков после запятой):")

