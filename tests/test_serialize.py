import pytest
from pathlib import Path
import sys

# Укажите абсолютный путь к папке src/lab08
sys.path.append("C:/Users/Анна/Desktop/misis_proga/python_labs/src/lab08")

from serialize import students_to_json, students_from_json
from models import Student


def test_serialize_students(tmp_path: Path):
    """Проверка сериализации и десериализации студентов"""
    
    test_file = tmp_path / "students_test.json"
    
    student_list = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петров Петр Петрович", "2001-08-20", "CS-02", 3.8)
    ]

    students_to_json(student_list, str(test_file))
    loaded_students = students_from_json(str(test_file))

    assert loaded_students[0].fio == student_list[0].fio
    assert loaded_students[1].fio == student_list[1].fio

def test_file_not_found():
    """Проверка ошибки при отсутствии файла"""
    
    with pytest.raises(FileNotFoundError):
        students_from_json("non_existent.json")

def test_wrong_file_extension():
    """Проверка ошибки при неправильном расширении файла"""
    
    with pytest.raises(ValueError):
        students_to_json([], "output.txt")
    
    with pytest.raises(ValueError):
        students_from_json("output.txt")

def test_invalid_json_format(tmp_path: Path):
    """Проверка ошибки при некорректном JSON формате"""
    
    invalid_json_file = tmp_path / "invalid.json"
    invalid_json_file.write_text("{invalid json", encoding="utf-8")
    
    with pytest.raises(ValueError):
        students_from_json(str(invalid_json_file))

def test_not_list_structure(tmp_path: Path):
    """Проверка ошибки при некорректной структуре данных"""
    
    with pytest.raises(TypeError):
        students_to_json("не список", str(tmp_path / "test.json"))

    not_list_file = tmp_path / "not_list.json"
    not_list_file.write_text('{}', encoding="utf-8")
    
    with pytest.raises(TypeError):
        students_from_json(str(not_list_file))

def test_not_student_objects():
    """Проверка ошибки при передаче не объектов Student"""
    
    with pytest.raises(TypeError):
        students_to_json([1, 2, 3], "test.json")