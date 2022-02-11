from myMatrix import MyMatrix


# Example input:
# 2 0.0001 # n epsilon
# 2 1 0 #extends matrix
# 1 2 0
def readmatrix(data):
    d = data.readline().strip().split()
    n = int(d[0])
    e = float(d[1])
    matrix = []
    for i in range(n):
        matrix.append(list(map(float, data.readline().strip().split())))
    return e, MyMatrix(matrix)


def print_vector(vector: list, msg: str | None) -> None:
    print(f"{msg} (", end="")
    print(*vector, sep="; ", end="")
    print(")")
