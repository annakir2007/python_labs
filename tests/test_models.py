import pytest
import sys
import os

# Добавляем путь к src/lab08
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
src_path = os.path.join(project_root, 'src', 'lab08')
sys.path.insert(0, src_path)

try:
    from models import Student
    print(f"Successfully imported from: {src_path}")
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Current sys.path: {sys.path}")
    # Пробуем альтернативный путь
    sys.path.insert(0, os.path.join(project_root, 'src'))
    try:
        from lab08.models import Student
        print("Imported from alternative path")
    except ImportError as e2:
        print(f"Alternative import also failed: {e2}")


class TestStudentValidation:
    """Проверки для валидации данных студента"""

    # Проверки для ФИО
    def test_fio_not_string(self):
        with pytest.raises(TypeError):
            Student(fio=123, birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_empty_string(self):
        with pytest.raises(ValueError):  # Исправлено на ValueError
            Student(fio="", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_only_spaces(self):
        with pytest.raises(ValueError):  # Исправлено на ValueError
            Student(fio="   ", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_contains_digits(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван123", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_single_word(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_lowercase_start(self):
        with pytest.raises(TypeError):
            Student(fio="иванов иван", birthdate="2000-01-01", group="SE-01", gpa=4.5)

    def test_fio_with_hyphen_valid(self):
        student_obj = Student(fio="Петров-Иванов Иван Иванович", birthdate="2000-05-15", group="SE-01", gpa=4.5)
        assert student_obj.fio == "Петров-Иванов Иван Иванович"

    # Проверки для даты рождения
    def test_birthdate_not_string_type(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate=20000101, group="SE-01", gpa=4.5)

    def test_birthdate_wrong_length_format(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-1", group="SE-01", gpa=4.5)

    def test_birthdate_incorrect_format(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000/01/01", group="SE-01", gpa=4.5)

    def test_birthdate_contains_letters(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван", birthdate="2000-ab-01", group="SE-01", gpa=4.5)

    def test_birthdate_invalid_month(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-13-01", group="SE-01", gpa=4.5)

    def test_birthdate_future_date_invalid(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2026-12-01", group="SE-01", gpa=4.5)

    # Проверки для GPA
    def test_gpa_not_float_type(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa="4.5")

    def test_gpa_below_zero(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=-1.0)

    def test_gpa_above_five(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=5.1)

    def test_gpa_boundary_values(self):
        Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE-01", gpa=0.0)
        Student(fio="Петров Петр", birthdate="2000-05-15", group="SE-01", gpa=5.0)

    # Проверки для группы
    def test_group_not_string_type(self):
        with pytest.raises(TypeError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group=101, gpa=4.5)

    def test_group_empty_string(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="", gpa=4.5)

    def test_group_only_spaces(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="   ", gpa=4.5)

    def test_group_too_short(self):
        with pytest.raises(ValueError):
            Student(fio="Иванов Иван", birthdate="2000-01-01", group="SE", gpa=4.5)


if __name__ == "__main__":
    # Простой тест импорта
    print("Testing import...")
    try:
        student = Student("Тестов Тест", "2000-01-01", "SE-01", 4.0)
        print(f"Student created: {student}")
    except Exception as e:
        print(f"Error creating student: {e}")