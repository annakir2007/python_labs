# <h1>ЛР1<h1>
# задание 1

![](./images/lb01/img_1_1.png)

# задание 2
![](./images/lb01/img_1_2.png)

# задание 3
![](./images/lb01/img_1_3.png)

# задание 4
![](./images/lb01/img_1_4.png)

# задание 5
![](./images/lb01/img_1_5.png)

# <h1>ЛР2<h1>

# задание 1

В 1 задании реализованы функции min_max() для нахождения минимума и максимума, unique_sorted() для сортировки уникальных значений по возрастанию, flatten() для "расплющивания" матрицы.

```
nums = []
n = int(input())
for i in range(n):
    s = input()
    if '.' in s:
        number = float(s)
    else:
        number = int(s)
    nums.append(number)
print(nums)

def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    return (min(nums), int(max(nums)))

def unique_sorted(nums):
    return sorted(set(nums))

def flatten(mat):
    listt = []
    for sublist in mat:#внутренние списки
        for item in sublist:#по элементам
            if not item.isdigit():#проверка на все числа
                return 'TypeError'
            else:
                listt.append(int(item))
    return listt

n = int(input("Сколько списков вы хотите создать? "))
mat = []
for i in range(n):
    elements = input(f"Введите числа для списка {i + 1} через пробел: ")
    inner_list = elements.split()
    mat.append(inner_list)

print(min_max(nums))
print(unique_sorted(nums))
print(flatten(mat))
```

# <h4>Функция 1<h4>

![](./images/lb02/img_2_1_1(1).png)

![](./images/lb02/img_2_1_1(2).png)

![](./images/lb02/img_2_1_1(3).png)

![](./images/lb02/img_2_1_1(4).png)

![](./images/lb02/img_2_1_1(5).png)

# <h4>Функция 2<h4>

![](./images/lb02/img_2_1_2(1).png)

![](./images/lb02/img_2_1_2(2).png)

![](./images/lb02/img_2_1_2(3).png)

![](./images/lb02/img_2_1_2(4).png)

# <h4>Функция 3<h4>

![](./images/lb02/img_2_1_3(1).png)

![](./images/lb02/img_2_1_3(2).png)

![](./images/lb02/img_2_1_3(3).png)

![](./images/lb02/img_2_1_3(4).png)

# задание 2

Во 2 задании реализованы функции transpose() для замены строк на столбцы, row_sums() для того, чтобы посчитать сумму по каждой строке, col_sums() для того, чтобы посчитать сумму по каждому столбцу.

```
n = int(input("Введите количество строк: "))
mat = []

# Ввод строк
for i in range(n):
    elements = input(f"Введите элементы для строки {i + 1} через пробел: ").split()
    mat.append(elements)

rows = len(mat)

# Если матрица пустая
if rows == 0:
    print('[]')
    exit()

cols = len(mat[0])

# Проверка, есть ли у каких-то строк меньшая длина (рваная матрица)
for i in range(rows):
    if len(mat[i]) != cols:
        print('ValueError')
        exit()

# Проверка, есть ли пустой элемент внутри матрицы
for i in range(rows):
    for j in range(len(mat[i])):  # перебираем только существующие элементы
        if mat[i][j] == '':
            print('ValueError')
            exit()

# Проверка, является ли матрица квадратной
if rows == cols:
    print('[0, 0]')
    exit()

def row_sums(matrix):
    result = []#суммы строк
    for row in matrix:
        converted = []#хранение чисел из строки
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
        if isinstance(total, float) and total.is_integer():#является ли сумма числом с плавающей точкой и при этом она равна целому числу
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
    
    row_len = len(mat[0])#количество столбцов
    for row in mat:#проверка на рванность матрицы
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
```

# <h4>Функция 1<h4>

![](./images/lb02/img_2_2_1(1).png)

![](./images/lb02/img_2_2_1(2).png)

![](./images/lb02/img_2_2_1(3).png)

![](./images/lb02/img_2_2_1(4).png)

![](./images/lb02/img_2_2_1(5).png)

# <h4>Функция 2<h4>

![](./images/lb02/img_2_2_2(1).png)

![](./images/lb02/img_2_2_2(2).png)

![](./images/lb02/img_2_2_2(3).png)

![](./images/lb02/img_2_2_2(4).png)

# <h4>Функция 3<h4>

![](./images/lb02/img_2_2_3(1).png)

![](./images/lb02/img_2_2_3(2).png)

![](./images/lb02/img_2_2_3(3).png)

![](./images/lb02/img_2_2_3(4).png)

# задание 3

В 3 задании реализована функция format_record() для записи информации о студенте(Инициалы, группа, gpa)

```
def format_record(rec):
    fio, group, gpa = rec#переменные кортежа

    fio = " ".join(fio.strip().split())#удаляем пробелы в начале и в конце строки фио;разделяем строку по пробелам;объединяем список слов обратно;остались только слова через 1 пробел
    group = group.strip()#Убираем пробелы в начале и конце строки с группой

    if fio == '' or group == '':
        return ValueError
    if not isinstance(gpa, (float, int)):#проверка: гпа число или нет
        raise TypeError("ГПА должно быть числом")
    parts = fio.split()#разделяем строку фио на отдельные слова
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать минимум фамилию и имя")
    surname = parts[0].capitalize()#записываем фамилию и делаем 1 буквы заглавной
    #Создаём инициалы
    initials = "".join([p[0].upper() + "." for p in parts[1:3]])#берём все слова, которые есть после фамилии; берём 1 букву для каждого слова из среза и делаем их заглавными;добавляем точку
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

# Примеры
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![](./images/lb02/img_2_3.png)