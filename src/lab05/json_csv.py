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
    #Проверка, что на вход подаётся точно json формат
    if not json_path.endswith('.json'):
        raise ValueError("Файл должен иметь расширение .json")

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
    
    #Проверка, что на вход подаётся csv-формат
    if not csv_path.endswith('.csv'):
        raise ValueError("Файл должен иметь расширение .csv")

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