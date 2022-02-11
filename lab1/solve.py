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
    print("Выразим вектор-столбец из уравнений")




