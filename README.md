# <h1>ЛР5<h1>

# задание A

Функции:  

json_to_csv — преобразует JSON-файл в CSV-файл. Он читает JSON, определяет колонки по первому объекту, заполняет отсутствующие поля пустыми строками и сохраняет данные в CSV.  

csv_to_json — преобразует CSV-файл обратно в JSON. Он читает CSV и создает список словарей, который затем сохраняет в JSON-файл.  

```
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Порядок колонок — как в первом объекте.
    """
    json_file = Path(json_path)#Создаем объект пути json_file, чтобы удобно работать с файлом

    # Проверка наличия файла
    if not json_file.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    # Чтение JSON
    with json_file.open("r", encoding="utf-8") as f:
        try:
            data = json.load(f)#Пытаемся загрузить содержимое файла как JSON
        except json.JSONDecodeError:
            raise ValueError("Некорректный формат JSON")
        
        # Проверка, что JSON - список
        if not isinstance(data, list):
            raise ValueError("JSON не является списком объектов")
        if len(data) == 0:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
        # Проверка, что все элементы - словари
        if not all(isinstance(item, dict) for item in data):#????
            raise ValueError("Некоторые элементы JSON не являются объектами")

        # Определение заголовков по первому элементу
        headers = list(data[0].keys())#???

        # Заполняем отсутствующие ключи
        for item in data:
            for key in headers:
                if key not in item:
                    item[key] = ""

    # Запись CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)#пишет словари как строки csv, зная названия колонок
        writer.writeheader()#записывает 1 строку с названиями колонок
        for row in data:
            writer.writerow(row)#каждый элемент пишется как строка csv

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Значения сохраняются как строки.
    """
    csv_file = Path(csv_path)#создаём объект пути для файла

    # Проверка наличия файла
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with open(csv_path, "r", encoding="utf-8") as f:
        try:
            # Проверка наличия данных
            # Используем csv.reader для определения наличия заголовка и данных
            reader = csv.reader(f)
            # Переместимся обратно в позицию для DictReader
            f.seek(0)
            # Используем DictReader
            dict_reader = csv.DictReader(f)
            headers = dict_reader.fieldnames

            if headers is None or len(headers) == 0:
                raise ValueError("CSV без заголовка")
            # Проверка наличия данных
            data_rows = list(dict_reader)
            if len(data_rows) == 0:
                raise ValueError("Пустой CSV")
        except csv.Error as e:
            raise ValueError(f"Ошибка при чтении CSV: {e}")

    # В JSON значения сохраняются как строки
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(data_rows, jf, ensure_ascii=False, indent=2)
json_to_csv(
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/samples/people.json',
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/out/output.csv'
)

csv_to_json(
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/samples/people.csv',
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/out/output.json'
)
```

# <h4>Задание А<h4>

people.json

![](./images/lb05/img_5_A_1.png)

people.csv

![](./images/lb05/img_5_A_2.png)

people_from_csv.json

![](./images/lb05/img_5_A_3.png)

people_from_json.csv

![](./images/lb05/img_5_A_4.png)

# задание B

Этот скрипт выполняет преобразование CSV-файла в формат Excel:

- Читает данные из указанного CSV-файла.  
- Создает новый Excel-файл с названием  
- Записывает в него заголовки и все строки из CSV.  
- Автоматически устанавливает ширину колонок так, чтобы в них полностью помещалось самое длинное содержимое, при этом минимальная ширина - 8 символов.  

Используется библиотека `openpyxl` для работы с Excel и встроенный модуль `csv`. 
```
# src/lab05/csv_xlsx.py
from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX. Использует openpyxl.
    - Первый ряд CSV - заголовки.
    - Лист называется "Sheet1".
    - Колонки - автоширина по длине текста (минимум 8 символов).
    
    Ошибки:
    - FileNotFoundError, если файл не существует.
    - ValueError при пустом или некорректном файле.
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    
    # Чтение CSV
    with csv_file.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if not rows:#проверка:если список rows пустой 
        raise ValueError("Пустой CSV файл.")
    header = rows[0]
    data_rows = rows[1:]
    
    if not header:
        raise ValueError("CSV без заголовка.")
    
    # Создание книги и листа
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    
    # Запись заголовков
    ws.append(header)
    
    # Запись данных
    for row in data_rows:
        ws.append(row)
    
    # Установка автоширины колонок
    for col_idx, col_cells in enumerate(zip(*rows)):
        max_length = max(len(str(cell)) for cell in col_cells)
        # Минимальная ширина 8
        adjusted_width = max(max_length + 2, 8)
        col_letter = ws.cell(row=1, column=col_idx + 1).column_letter
        ws.column_dimensions[col_letter].width = adjusted_width
    
    # Сохранение файла
    xlsx_path_obj = Path(xlsx_path)
    wb.save(str(xlsx_path_obj))

csv_to_xlsx(
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/samples/people.csv',
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/out/output.xlsx'
)
```

# <h4>Задание B<h4>

csv-файл:

![](./images/lb05/img_A_2.png)

xlsx-файл:

![](./images/lb05/img_5_B_1.png)

Если файл пустой:

![](./images/lb05/img_5_B_2.png)

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
    # Если вход - кортеж, преобразуем его в список
    if isinstance(mat, tuple):
        mat = list(mat)

    listt = []
    for sublist in mat:  # могут быть и списки, и кортежи
        # Определяем возможные вложенные кортежи/списки
        if isinstance(sublist, (list, tuple)):
            for item in sublist:
                # Проверка, является ли item числом или строкой
                if isinstance(item, str):#если элемент - строка
                    if not item.isdigit():
                        return 'TypeError'
                    else:
                        listt.append(int(item))
                elif isinstance(item, (int, float)):#если элемент - число
                    listt.append(item)
                else:
                    return 'TypeError'
        else:
            # Если внутри не список/кортеж, возможно, ошибка
            return 'TypeError'
    return listt

n = int(input("Сколько списков вы хотите создать? "))
mat = []
for i in range(n):
    elements = input(f"Введите числа для списка {i + 1} через пробел: ")
    inner_list = elements.split()
    mat.append(inner_list)
print(flatten([(1, 2), (3, 4)]))
print(flatten([[1, 2], [3, 4]]))
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

# <h1>ЛР3<h1>

# задание A

В задании А реализованы 3 функции, которые позволяют:

превратить любой текст в однородный вид (normalize),
разбить текст на слова (tokenize),
посчитать, как часто встречаются слова (count_freq),
узнать, какие слова встречаются чаще всего (top_n).

```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # Заменяем управляющие символы \r, \n, \t на пробелы
    text = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

    # Замена ё/Ё на е/Е
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    # Применение casefold (если требуется) с обработкой ошибок
    '''Если мы хотим делать все буквы маленькими, то сначала пытаемся использовать casefold(), которая очень хорошо переводит все буквы в маленькие и делает слова одинаковыми.
Если casefold() не работает, тогда используем lower() — тоже превращает буквы в маленькие.'''
    if casefold:
        try:
            text = text.casefold()
        except AttributeError:
            text = text.lower()

    # Схлопываем подряд идущие пробелы в один и удаляем пробелы по краям
    result_chars = []#сюда будем добавлять буквы
    prev_space = False#флажок, который говорит, был ли предыдущий символ пробелом.
    for ch in text:
        if ch.isspace():#Если символ — это пробел или похожий знак (isspace() значит — пробел, табуляция или перевод строки),
            if not prev_space:#если не пробел --> True
                result_chars.append(' ')
                prev_space = True
        else:
            result_chars.append(ch)#не является пробелом, значит добавляем текущий символ ch в итоговый список.
            prev_space = False#обнуляем флаг
    normalized_text = ''.join(result_chars).strip()#удаление лишних пробелов с начала и с конца
    #Объединяем список символов result_chars в строку.
    return normalized_text


def tokenize(text: str) -> list[str]:
    tokens = []#список хранения итоговых токенов
    current_word = []#список символов текущего слова

    def is_word_char(c):#возвращает True, если символ - буква, цифра, подчёркивание или дефис
        return c.isalnum() or c in ['_', '-']

    for c in text:
        if is_word_char(c):
            current_word.append(c)
        elif c == '-':
            # дефис внутри слова — добавляем, если слово уже есть
            if current_word:
                current_word.append(c)
        else:
            # разделитель
            if current_word:
                tokens.append(''.join(current_word))#Объединяет символы в строку и добавляет в список tokens
                current_word = []#сброс списка для следующего слова
    #После завершения цикла, если есть ещё незанесённое слово, добавляем его.
    if current_word:
        tokens.append(''.join(current_word))
    return tokens

#для каждого токена увеличивает значение по ключу token на 1
def count_freq(tokens: list[str]) -> dict:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq#словарь, где ключ — токен, значение — количество

#сортирует пары в словаре по убыванию частоты(-item[1])(если равны, по алфавиту(item[0])); возвращает первые n элементов из отсортированного списка
def top_n(freq: dict, n: int = 5) -> list:
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

#тесты

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]
```

# <h4>Задание А<h4>

![](./images/lb03/img_task_A.png)

# задание B

Скрипт читает одну строку текста, вызывает функции из lib/text.py и печатает:

Всего слов:
Уникальных слов:
Топ-5:
Частоту повторений слов:
```
import sys
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lib")
from text import normalize, tokenize, count_freq, top_n

text = input()
norm_txt = normalize(text)
token = tokenize(norm_txt)
freq = count_freq(token)#создает словарь, где ключ — слово, значение — сколько раз оно встречается.
top_5 = top_n(freq, n=5)#получает список из 5 наиболее часто встречающихся слов.
print(f"Всего слов: {len(token)}")
print(f"Уникальных слов: {len(freq.keys())}")# длина всех ключей в словаре
print(f"Топ-5:")
for i in top_5:
    print(f"{i[0]}:{i[1]}")
```

# <h4>Задание B<h4>

![](./images/lb03/img_text_stats.png)

# <h1>ЛР4<h1>

# задание A

1.Открывает файл на чтение в указанной кодировке.  
2.Обрабатывает ошибки.  
3.Создаёт/перезаписывает CSV с разделителем.  
4.Создаёт родительские директории, если их нет.  

```
from pathlib import Path
import csv
from typing import Sequence, Iterable, Union

PathLike = Union[str, Path]

#принимает на вход путь к файлу(path) и кодировку(encoging)
def read_text(path: PathLike, encoding: str = "utf-8") -> str:
    """
    Считать текст из файла как одну строку.

    Args:
        path: Путь к файлу (строка или Path).
        encoding: Кодировка для чтения (по умолчанию "utf-8").

    Returns:
        Содержимое файла в виде строки.

    Пример выбора другой кодировки:
        read_text("file.txt", encoding="cp1251")
    """
    p = Path(path)#создаёт объект path из переменной path и записывает в переменную p
    with p.open('r', encoding=encoding) as file:
        content = file.read()#читает файл целиком
        #возвращается содержимое или пустая строка, если файл пустой
        return content if content is not None else ""
    # Если файл пустой, content будет ""

def parent_dir(path: PathLike) -> None:
    """
    Создаёт родительские директории указанного пути, если их нет.

    Args:
        path: Путь к файлу (строка или Path).
    """
    p = Path(path)
    parent = p.parent#Получает родительскую директорию пути
    if not parent.exists():#exists() возвращает True, если папка(или файл) есть в файловой системе
        parent.mkdir(parents=True, exist_ok=True)
#parents=True — если надо, создаст все промежуточные папки, которых нет
#Параметр exist_ok=True — не выдаст ошибку, если папка уже существует.

def write_csv(rows, path, header=None):
    """
    Записать данные в CSV файл с разделителем ','.

    Args:
        rows: Список строк (кортежей или списков) с данными.
        path: Путь к CSV файлу (строка или Path).
        header: Кортеж заголовка (имён столбцов), если указан — записывается первой строкой.

    Raises:
        ValueError: Если длины строк в rows не совпадают.
    """
    if not rows:#Проверка, пустой ли список rows
        # Нечего проверять, но если header есть — файл будет с одним заголовком
        length = len(header) if header is not None else 0
    else:
        length = len(rows[0])#length — длина первой строки в списке данных.
        #i — индекс текущей строки в списке; r — сама текущая строка (список или кортеж с элементами)
        for i, r in enumerate(rows):
            if len(r) != length:
                raise ValueError
#Перед созданием файла вызывается функция, чтобы убедиться, что папка для файла существует. Если нет — она будет создана.
    parent_dir(path)

    p = Path(path)
    #f — переменная, которая ссылается на открытый файловый объект
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)#принимает файловый объект и умеет записывать данные в файл в формате CSV (то есть строки с разделителями)
        if header is not None:
            if len(header) != length:
                raise ValueError
            writer.writerow(header)#Если заголовок указан, вызывается writer.writerow(header) — запись заголовка как первой строки CSV-файла.
        for row in rows:#Итерация по всем строкам данных rows
            writer.writerow(row)
#все данные записываются построчно под заголовком(если он был)

#пример для README
if __name__ == "__main__":
    try:
        text = read_text("data/input.txt")
        print("Прочитан текст (первые 100 символов):")
        print(text[:100])
    except Exception as e:
        print("Ошибка при чтении файла:", e)

    # запись CSV с заголовком и несколькими строками
    try:
        #создаём массив данных row, записываем их в файл с заголовками
        rows = [("test", 3), ("apple", 3), ("banana", 5), ("orange", 2)]
        write_csv(rows, "data/output.csv", header=("word", "count"))
        print("CSV записан: data/output.csv")
    except Exception as e:
        print("Ошибка при записи CSV:", e)
```

# <h4>Задание А<h4>
Если в файле что-то написано:

![](./images/lb04/img_A_2.png)

Если файл пустой:

![](./images/lb04/img_A_1.png)

# задание B

Скрипт читает input.txt , вызывает функции из lib/text.py и печатает:  
Всего слов:  
Уникальных слов:  
Топ-5:  
Частоту повторений слов:  
```
import sys
import argparse
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lib")
from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

def main():
    # Создаем объект для чтения аргументов командной строки
    parser = argparse.ArgumentParser()

    #Считаем аргументы:
    # --in — входной файл("data/input.txt")
    parser.add_argument("--in", dest="input_file", default="data/input.txt")
    # --out — выходной файл("data/report.csv")
    parser.add_argument("--out", dest="output_file", default="data/report.csv")
    # --encoding — кодировка файла("utf-8")
    parser.add_argument("--encoding", default="utf-8")
    
    # Распарсиваем аргументы из командной строки
    args = parser.parse_args()

    # Попытка открыть и прочитать входной файл
    try:
        text = read_text(args.input_file)
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit()  # выходим из программы при ошибке

    # Обрабатываем текст: делаем его нормальным и делим на слова
    text = normalize(text)
    tokens = tokenize(text)

    # Подсчитываем, сколько раз каждое слово встречается
    freq = count_freq(tokens)

    # Сортируем слова по количеству встреч
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Создаем таблицу данных для отчета
    header = ["word", "count"]
    data = [[word, count] for word, count in sorted_words]
    # Записываем результат в CSV файл
    write_csv(data, args.output_file, header)

    # Выводим статистику
    total_words = sum(freq.values())  # Общее число всех слов
    unique_words = len(freq)           # Количество уникальных слов
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_n(freq, 5):
        print(f"{word} - {count}")

if __name__ == "__main__":
    main()
```

# <h4>Задание B<h4>

![](./images/lb04/img_B_1.png)

Содержимое файла report.csv

![](./images/lb04/img_2_B_2.png)

Содержимое файла input.txt

![](./images/lb04/img_2_B_3.png)