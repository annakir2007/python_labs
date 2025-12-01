import json
from pathlib import Path
from models import *


def students_to_json(student_list, file_path):
    """Сохранение списка студентов в JSON-файл"""

    file_obj = Path(file_path)

    if not str(file_obj).endswith(".json"):
        raise ValueError("неверный тип файла, файл должен иметь расширение json")

    if not isinstance(student_list, list):
        raise TypeError("student_list должно быть списком объектов.")

    for student in student_list:
        if not isinstance(student, Student):
            raise TypeError("все элементы списка должны быть объектами Student.")

    student_data = []
    for student in student_list:
        student_data.append(student.to_dict())

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(student_data, file, ensure_ascii=False, indent=2)


def students_from_json(file_path):
    """Загрузка списка студентов из JSON-файла"""

    file_obj = Path(file_path)

    if not str(file_obj).endswith(".json"):
        raise ValueError("неверный тип файла, файл должен иметь расширение json")
    
    if not file_obj.exists(): 
        raise FileNotFoundError("файл не найден")

    with open(file_obj, 'r', encoding='utf-8') as file:
        try:
            json_data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("некорректный формат json-файла")
        except UnicodeDecodeError:
            raise ValueError("Некорректная кодировка файла")

    if not isinstance(json_data, list):
        raise TypeError("json-файл должен содержать список студентов.")

    result_list = []
    for student_dict in json_data:
        if not isinstance(student_dict, dict):
            raise TypeError("каждый студент в json-файле должен быть словарем.")
        result_list.append(Student.from_dict(student_dict))

    return result_list