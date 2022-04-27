import math

from numpy.polynomial import Polynomial as P


def getLagrangePolinom(points: list[tuple[float, float]]) -> P:
    ans = P([0])
    for i in range(len(points)):
        t = P([points[i][1]])
        for j in range(len(points)):
            if i != j:
                t *= P([-points[j][0], 1]) // (points[i][0] - points[j][0])
        ans += t
    return ans


def getNewtonPolinom(points: list[tuple[float, float]], x_search=None) -> P:
    t = points[1][0] - points[0][0]
    if all([t - points[i + 1][0] + points[i][0] < 1e-6 for i in range(len(points) - 1)]):
        return getNewtonPolinomUseConstSub(points, x_search)
    # при возможности применяем конечные разности, иначе интерполяция по Ньютону
    gk = P([points[0][1]])
    for k in range(len(points) - 1):
        ak = points[k + 1][1] - gk(points[k + 1][0])
        for i in range(k + 1):
            ak /= points[k + 1][0] - points[i][0]
        t = P([ak])
        for i in range(k + 1):
            t *= P([-points[i][0], 1])
        gk += t
    return gk


def getNewtonPolinomUseConstSub(points: list[tuple[float, float]], x_search=None) -> P:
    points.sort()
    if x_search is None:
        return NewtonFront(points)

    for i in range(len(points) - 1):
        if x_search <= points[i + 1][0]:
            return NewtonFront(points[i:]) if i < len(points) / 2 else NewtonBack(points)
    return NewtonBack(points)


def getConstSubs(points: list[tuple[float, float]]) -> list[list[float]]:
    ans = [[] for _ in range(len(points) - 1)]
    for i in range(len(points) - 1):
        ans[i].append(points[i + 1][1] - points[i][1])

    for j in range(1, len(points) - 1):
        for i in range(len(points) - 1 - j):
            ans[i].append(ans[i + 1][j - 1] - ans[i][j - 1])

    return ans


def NewtonFront(points: list[tuple[float, float]]) -> P:
    subs = getConstSubs(points)
    ans = P([points[0][1]])
    t = P([-points[0][0], 1]) // (points[1][0] - points[0][0])
    g = 1
    for i in range(len(points) - 1):
        g *= t - i
        ans += g * subs[0][i] // math.factorial(i + 1)
    return ans


def NewtonBack(points: list[tuple[float, float]]) -> P:
    subs = getConstSubs(points)
    ans = P([points[len(points) - 1][1]])
    t = P([-points[len(points) - 1][0], 1]) // (points[1][0] - points[0][0])
    g = 1
    for i in range(len(points) - 1):
        g *= t + i
        ans += g * subs[len(points) - i - 2][i] // math.factorial(i + 1)
    return ans


def getGaussPolinom(points: list[tuple[float, float]]):
    pass


if __name__ == '__main__':
    print(getConstSubs([(.1, 1.25), (0.2, 2.38), (.3, 3.79), (.4, 5.44), (.5, 7.14)]))
    k = getNewtonPolinom([(.1, 1.25), (0.2, 2.38), (.3, 3.79), (.4, 5.44), (.5, 7.14)])
    print(k)
    k = getLagrangePolinom([(.1, 1.25), (0.2, 2.38), (.3, 3.79), (.4, 5.44), (.5, 7.14)])
    print(k)
    print(k(0.47))
