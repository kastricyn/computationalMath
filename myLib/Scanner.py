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
    def getListFloat(min: float = -inf, max: float = inf, greeting: str = "Введите пожалуйста") -> float:
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


if __name__ == '__main__':
    Scanner.getInt(-10, -5)
    Scanner.getFloat(-10, -5)