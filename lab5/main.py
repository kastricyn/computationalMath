import numpy as np

from interpolation import getNewtonPolinom, getLagrangePolinom

from math import pi, sqrt
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print("Введите кол-во точек, или 0, чтобы посчитать занчение sin(x) при x из (0; pi/2)")
    n = int(input())
    print("Введите точку, в которой необходимо вычислить значение функции:")
    x = float(input())

    points: list[tuple] = []
    if n != 0:
        print(f"Введите {n} точек (по одной точке на каждой строке, разделяя координаты пробелом)")
        for _ in range(n):
            points.append(tuple(map(float, input().split())))
    else:
        points.append((0, 0))
        points.append((pi / 6, 0.5))
        points.append((pi / 4, sqrt(2) / 2))
        points.append((pi / 3, sqrt(3) / 2))

    lagrange_polinom = getLagrangePolinom(points)
    print("Интерполяционный многочлен по Лагранжу: f(x) = ", lagrange_polinom)
    print("Значение f(x): ", lagrange_polinom(x))

    newton_polinom = getNewtonPolinom(points, x)
    print("Интерполяционный многочлен по Ньютону: f(x) = ", newton_polinom)
    print("Значение f(x): ", newton_polinom(x))

    X = [point[0] for point in points]
    Y = [point[1] for point in points]
    plt.scatter(X, Y, marker='o', c="w", linewidths=2, edgecolors='r')
    linspace = np.linspace(min(X) - 0.1 * abs(max(X) - min(X)), max(X) + 0.1 * abs(max(X) - min(X)), 100)

    plt.vlines(x, min(lagrange_polinom(linspace)), max(lagrange_polinom(linspace)), linestyles="dashed", label="Искомое значение")
    plt.plot(linspace, lagrange_polinom(linspace), c='g', label="Лагранж придумал")
    plt.plot(linspace, newton_polinom(linspace), c='b', label="Ньютон придумал")
    plt.legend()
    plt.grid()
    plt.show()
