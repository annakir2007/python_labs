import json
import csv
from pathlib import Path


def json_to_csv(src_path: str, dst_path: str) -> None:
    """Конвертирует JSON файл в CSV файл."""
    src = Path(src_path)
    dst = Path(dst_path)

    if not src.exists():
        raise FileNotFoundError(f"Source file {src_path} not found")

    try:
        with src.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

    if not data:
        raise ValueError("JSON file is empty")

    if not isinstance(data, list):
        raise ValueError("JSON data should be a list of objects")

    # Получаем все возможные ключи из всех объектов
    fieldnames = set()
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Each item in JSON should be a dictionary")
        fieldnames.update(item.keys())

    fieldnames = sorted(fieldnames)

    with dst.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        # Для каждой записи создаем строку с заполненными всеми полями
        for item in data:
            row = {field: item.get(field, "") for field in fieldnames}
            writer.writerow(row)


def csv_to_json(src_path: str, dst_path: str) -> None:
    """Конвертирует CSV файл в JSON файл."""
    src = Path(src_path)
    dst = Path(dst_path)

    if not src.exists():
        raise FileNotFoundError(f"Source file {src_path} not found")

    data = []
    try:
        with src.open("r", encoding="utf-8") as f:
            # Проверяем, что файл не пустой
            content = f.read().strip()
            if not content:
                raise ValueError("CSV file is empty")

            # Возвращаемся в начало и читаем как CSV
            f.seek(0)
            reader = csv.DictReader(f)

            if not reader.fieldnames:
                raise ValueError("CSV file has no headers")

            for row in reader:
                # Если есть хоть одно непустое значение, добавляем
                if any(value.strip() for value in row.values() if value):
                    data.append(row)

    except csv.Error as e:
        raise ValueError(f"Invalid CSV format: {e}")

    if not data:
        raise ValueError("No valid data found in CSV file")

    with dst.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
