from pathlib import Path
import csv
from typing import Sequence, Iterable, Union

PathLike = Union[str, Path]


# принимает на вход путь к файлу(path) и кодировку(encoging)
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
    p = Path(path)  # создаёт объект path из переменной path и записывает в переменную p
    with p.open("r", encoding=encoding) as file:
        content = file.read()  # читает файл целиком
        # возвращается содержимое или пустая строка, если файл пустой
        return content if content is not None else ""
    # Если файл пустой, content будет ""


def parent_dir(path: PathLike) -> None:
    """
    Создаёт родительские директории указанного пути, если их нет.

    Args:
        path: Путь к файлу (строка или Path).
    """
    p = Path(path)
    parent = p.parent  # Получает родительскую директорию пути
    if (
        not parent.exists()
    ):  # exists() возвращает True, если папка(или файл) есть в файловой системе
        parent.mkdir(parents=True, exist_ok=True)


# parents=True — если надо, создаст все промежуточные папки, которых нет
# Параметр exist_ok=True — не выдаст ошибку, если папка уже существует.


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
    if not rows:  # Проверка, пустой ли список rows
        # Нечего проверять, но если header есть — файл будет с одним заголовком
        length = len(header) if header is not None else 0
    else:
        length = len(rows[0])  # length — длина первой строки в списке данных.
        # i — индекс текущей строки в списке; r — сама текущая строка (список или кортеж с элементами)
        for i, r in enumerate(rows):
            if len(r) != length:
                raise ValueError
    # Перед созданием файла вызывается функция, чтобы убедиться, что папка для файла существует. Если нет — она будет создана.
    parent_dir(path)

    p = Path(path)
    # f — переменная, которая ссылается на открытый файловый объект
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(
            f
        )  # принимает файловый объект и умеет записывать данные в файл в формате CSV (то есть строки с разделителями)
        if header is not None:
            if len(header) != length:
                raise ValueError
            writer.writerow(
                header
            )  # Если заголовок указан, вызывается writer.writerow(header) — запись заголовка как первой строки CSV-файла.
        for row in rows:  # Итерация по всем строкам данных rows
            writer.writerow(row)


# все данные записываются построчно под заголовком(если он был)

# пример для README
if __name__ == "__main__":
    try:
        text = read_text("data/input.txt")
        print("Прочитан текст (первые 100 символов):")
        print(text[:100])
    except Exception as e:
        print("Ошибка при чтении файла:", e)

    # запись CSV с заголовком и несколькими строками
    try:
        # создаём массив данных row, записываем их в файл с заголовками
        rows = [("test", 3), ("apple", 3), ("banana", 5), ("orange", 2)]
        write_csv(rows, "data/output.csv", header=("word", "count"))
        print("CSV записан: data/output.csv")
    except Exception as e:
        print("Ошибка при записи CSV:", e)
