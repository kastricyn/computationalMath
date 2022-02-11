from numpy import inf

from lab1.myIO import print_vector
from myMatrix import MyMatrix


def simple_iteration(extend_matrix: MyMatrix, e: float) -> None:
    print(f"Решаем систему уравнений с точностю {e}  и расширенной матрицой:")
    extend_matrix.print()
    if not extend_matrix.check_diagonal_dominance():
        print("Условие преобладания диагональных элементов не выполняется, попробуем переставить уравнения местами.")
        extend_matrix.try_move_equations()
        if extend_matrix.check_diagonal_dominance():
            extend_matrix.print()
            print("Теперь условие преобладания диагональных элементов выполняется.")
        else:
            print("К сожалению, удовлетворяющей перестановки не нашлось")
    else:
        print("Условие преобладания диагональных элементов выполняется.")
    print("Выразим вектор-столбец системы из уравнений:")
    equation_system: MyMatrix = extend_matrix.get_vector_column_system()
    equation_system.print()

    count = 1
    ans = [0] * equation_system.n
    before_ans = equation_system.insert_vector_into_vector_column_system([0] * equation_system.n)
    fallibility = [inf]
    while not max(fallibility) < e:
        count += 1
        ans = equation_system.insert_vector_into_vector_column_system(before_ans)
        fallibility = [
            abs(ans[i] - before_ans[i]) for i in range(equation_system.n)
        ]
        before_ans = ans


    print_vector(ans, "результирующий вектор:")
    print(f"решение найдено за {count} итераций")
    print_vector(fallibility, "вектор погрешности:")
