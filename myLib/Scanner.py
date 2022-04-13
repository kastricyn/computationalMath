import sys
from math import inf


class Scanner:
    @staticmethod
    def getInt(min: float = -inf, max: float = inf, greeting: str = "Введите пожалуйста целое") -> int:
        t = ""
        if min >= max:
            min, max = max, min

        warning = f"Должно быть"
        sub_greeting = f" число между {min} и {max}"

        print(greeting + sub_greeting)
        while True:
            try:
                t = int(input())
                if min <= t <= max:
                    return t
                else:
                    print(warning + sub_greeting)
            except ValueError:
                print("Похоже это не целое число, попробуйте ещё раз")

    @staticmethod
    def getFloat(min: float = -inf, max: float = inf, greeting: str = "Введите пожалуйста") -> float:
        t = ""
        if min >= max:
            min, max = max, min

        warning = f"Должно быть целое"
        sub_greeting = f" число между {min} и {max}"

        print(greeting + sub_greeting)
        while True:
            try:
                t = float(input())
                if min <= t <= max:
                    return t
                else:
                    print(warning + sub_greeting)
            except ValueError:
                print("Похоже это не число, попробуйте ещё раз")

    @staticmethod
    def getFloatList(n: int = None, greeting: str = "", input=sys.stdin, output=sys.stdout, erroutput=sys.stderr) -> \
            list[float]:
        if n is None:
            print(
                f"Введите числа в строку, разделяя их пробелами {greeting}:",
                file=output)
        else:
            print(
                f"Введите {n} чисел(-ла) в строку, разделяя их пробелами {greeting}:",
                file=output)

        t = list(map(float, input.readline().strip().split()))
        while n is not None and len(t) != n:
            print(
                f"Что-то пошло не так, должно быть {n} элементов в строке, а получлось {len(t)}. Введите ещё раз {n} чисел:",
                file=erroutput)
            t = list(map(float, input.readline().strip().split()))
        return t


if __name__ == '__main__':
    x = Scanner.getFloatList(greeting="-- x")
    y = Scanner.getFloatList(greeting="-- y", n=len(x))
