n = int(input("Введите количество строк: "))
mat = []

# Ввод строк
for i in range(n):
    elements = input(f"Введите элементы для строки {i + 1} через пробел: ").split()
    mat.append(elements)

rows = len(mat)

# Если матрица пустая
if rows == 0:
    print("[]")
    exit()

cols = len(mat[0])

# Проверка, есть ли у каких-то строк меньшая длина (рваная матрица)
for i in range(rows):
    if len(mat[i]) != cols:
        print("ValueError")
        exit()

# Проверка, есть ли пустой элемент внутри матрицы
for i in range(rows):
    for j in range(len(mat[i])):  # перебираем только существующие элементы
        if mat[i][j] == "":
            print("ValueError")
            exit()

# Проверка, является ли матрица квадратной
if rows == cols:
    print("[0, 0]")
    exit()


def row_sums(matrix):
    result = []  # суммы строк
    for row in matrix:
        converted = []  # хранение чисел из строки
        for item in row:
            # Пытаемся преобразовать сначала в int
            try:
                num = int(item)
                converted.append(num)
            except ValueError:
                # Если не получилось, пробуем float
                try:
                    num = float(item)
                    converted.append(num)
                except ValueError:
                    return "ValueError"
        # Суммируем
        total = sum(converted)
        # Если сумма — целое число, выводим как int
        if (
            isinstance(total, float) and total.is_integer()
        ):  # является ли сумма числом с плавающей точкой и при этом она равна целому числу
            total = int(total)
        result.append(total)
    return result


print(row_sums(mat))


def transpose(matrix):
    # Проверка, что матрица не пуста и все строки одинаковой длины
    if len(matrix) == 0:
        return []

    row_length = len(matrix[0])  # количество столбцов
    # Проверка на рваность
    for row in matrix:
        if len(row) != row_length:
            return "ValueError"

    # Создаем новую матрицу для транспонированных данных
    transposed = []
    # Перебираем каждый столбец (по индексу)
    for i in range(row_length):
        new_row = []
        # Собираем элементы из каждого ряда в этот столбец
        for row in matrix:
            new_row.append(row[i])
        transposed.append(new_row)
    return transposed


print(transpose(mat))


def col_sums(mat):
    if len(mat) == 0:
        return []

    row_len = len(mat[0])  # количество столбцов
    for row in mat:  # проверка на рванность матрицы
        if len(row) != row_len:
            return "ValueError"

    numeric_mat = []
    for row in mat:
        numeric_row = []
        for item in row:
            try:
                num = int(item)
            except ValueError:
                try:
                    num = float(item)
                except ValueError:
                    return "ValueError"
            numeric_row.append(num)
        numeric_mat.append(numeric_row)
    return [sum(row[j] for row in numeric_mat) for j in range(row_len)]


print(col_sums(mat))
