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
    #проверка, что на входе точно csv
    if not csv_path.endswith('.csv'):
        raise ValueError("Файл должен иметь расширение .csv")

    # Чтение CSV
    with csv_file.open("r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if not rows:#Проверка: если список rows пустой 
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
    #Автоматическая настройка ширины каждой колонки так,
    #  чтобы она соответствовала длине наибольшего содержимого в этой колонке,
    #  с учетом минимальной ширины 8 символов.
    for col_idx, col_cells in enumerate(zip(*rows)):
        '''
        col_idx: порядковый номер колонки (0, 1, 2, ...).
col_cells: кортеж значений в этой колонке (например, ('Имя', 'Аня', 'Боря')).
rows — это список списков, где каждый вложенный список — строка CSV.
*rows — распаковка списка rows в отдельные аргументы функции.
zip() объединяет эти строки поэлементно, создавая кортежи, содержащие элементы из каждой строки, соответствующие одной колонке.
        '''
        max_length = max(len(str(cell)) for cell in col_cells)#Для каждой колонки ищем длину самой длинной ячейки.
        # Минимальная ширина 8
        adjusted_width = max(max_length + 2, 8)
        col_letter = ws.cell(row=1, column=col_idx + 1).column_letter#метод который возращает ячейку по заданным координатам(преобразует цифру столбца в букву столбца)
        ws.column_dimensions[col_letter].width = adjusted_width#устанавливаем ширину текущей колонки
    
    # Сохранение файла
    xlsx_path_obj = Path(xlsx_path)
    wb.save(str(xlsx_path_obj))

csv_to_xlsx(
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/samples/people.csv',
    'C:/Users/Анна/Desktop/misis_proga/python_labs/data/out/output.xlsx'
)