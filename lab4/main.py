from OrdinaryLeastSquares.PolinomApproximation import PolinomApproximate
from OrdinaryLeastSquares.ExpApproximate import ExpApproximate
from OrdinaryLeastSquares.LogApproximate import LogApproximate
from OrdinaryLeastSquares.PowApproximate import PowApproximate

if __name__ == '__main__':
    print("Введите колв-во точек:")
    n = int(input())
    print("Введите точки (по одной точке на каждой строке, разделяя координаты пробелом)")
    points: list[tuple] = []
    for _ in range(n):
        points.append(tuple(map(float, input().split())))

    approximations = dict()
    approximations['Линейная'] = PolinomApproximate(points, 1)
    approximations['Квадратичная'] = PolinomApproximate(points, polinom_degree=2)
    approximations['Кубическая'] = PolinomApproximate(points, polinom_degree=3)
    approximations['Экспоненциальная'] = ExpApproximate(points)
    approximations['Логарифмическая'] = LogApproximate(points)
    approximations['Степенная'] = PowApproximate(points)

    best_approx_key = "Линейная"
    for key in approximations:
        print(f"{key} апроксимация:")
        print(f"\t f(x) = {approximations[key]}")
        print(f"\t Среднеквадратичное отклонение: {approximations[key].metrix['sigma']}")
        print(f"\t Все характеристики: {approximations[key].metrix}")

        if approximations[best_approx_key].metrix["sigma"] > approximations[key].metrix['sigma']:
            best_approx_key = key

    print(f"{best_approx_key} аппроксимация --- лучшая")


