import sys

import myIO as io
from lab1.solve import simple_iteration
from myMatrix import InvalidArrayForCreateMatrix

if __name__ == '__main__':
    filename = input("Введите путь до файла или переведите строку, чтобы продолжить работать с консолью:").strip()
    # todo: что если файла нет или нет доступа к файлу?
    try:
        if filename:
            e, matrix = io.readmatrix(open(filename))
        else:
            e, matrix = io.readmatrix(sys.stdin)
    except InvalidArrayForCreateMatrix:
        print("Проверьте входные данные")
    else:
        simple_iteration(matrix, e)
