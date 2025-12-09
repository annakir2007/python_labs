import csv
from pathlib import Path
import sys
from datetime import date
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lab08")
from models import Student

class Group:
    def __init__(self, storage_path: str):
        # Полный путь к файлу
        self.path = Path(storage_path)
        # Создаем директорию, если она не существует
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read_all(self):
        # Создаем файл если не существует
        if not self.path.exists():
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])
            return []  # Файл только что создан

        students = []
        
        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    students.append(row)
    
        return students

    def _ensure_storage_exists(self, students: list):
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(students)

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        students = self._read_all()

        # преобразуем date в строку если нужно
        birthdate_value = student.birthdate
        if isinstance(student.birthdate, date):
            birthdate_value = student.birthdate.strftime("%Y-%m-%d")

        student_dict = {
            "fio": student.fio,
            "birthdate": birthdate_value,
            "group": student.group,
            "gpa": student.gpa,
        }

        students.append(student_dict)
        self._ensure_storage_exists(students)

    def find(self, substr: str):
        rows = self._read_all()
        return [r for r in rows if substr.lower() in r["fio"].lower()]

    def remove(self, fio: str):
        rows = self._read_all()

        for i, r in enumerate(rows):
            if r["fio"] == fio:
                rows.pop(i)
                self._ensure_storage_exists(rows)
                return True

        return False

    def update(self, fio: str, **fields):
        rows = self._read_all()

        for row in rows:
            if row["fio"] == fio:
                # Если передали date, преобразуем в строку
                for key, value in fields.items():
                    if key == "birthdate" and isinstance(value, date):
                        fields[key] = value.strftime("%Y-%m-%d")
                row.update(fields)
                self._ensure_storage_exists(rows)
                return True

        return False

    @staticmethod
    def find_max(array):
        if not array:
            return 0
        m = -float("inf")
        for i in range(len(array)):
            if array[i] > m:
                m = array[i]
        return m

    @staticmethod
    def find_min(array):
        if not array:
            return 0
        m = float("inf")
        for i in range(len(array)):
            if array[i] < m:
                m = array[i]
        return m

    def stats(self):
        students = self._read_all()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5": [],
            }

        groups = [i["group"] for i in students]
        gpas = [float(student["gpa"]) for student in students]
        group_counts = {group: groups.count(group) for group in set(groups)}
        
        # Сортируем по GPA (по убыванию)
        sorted_students = sorted(students, key=lambda s: float(s["gpa"]), reverse=True)
        top_5 = sorted_students[:5]
        top_5_list = [{"fio": s["fio"], "gpa": s["gpa"]} for s in top_5]

        return {
            "count": len(students),
            "min_gpa": self.find_min(gpas),
            "max_gpa": self.find_max(gpas),
            "avg_gpa": sum(gpas) / len(students) if students else 0,
            "groups": group_counts,
            "top_5": top_5_list,
        }


# ТЕСТЫ
if __name__ == "__main__":
    print("=" * 50)
    print("НАЧАЛО ТЕСТОВ")
    print("=" * 50)
    
    #Создаем объект Group с новым путем и названием файла
    #Указываем полный путь к файлу students.csv
    csv_path = r"C:\Users\Анна\Desktop\misis_proga\python_labs\data\lab09\students.csv"
    group = Group(csv_path)
    
    # 1. Проверяем список (должен быть пустым или содержать данные)
    print("\n1. Список студентов (начальный):")
    students_list = group.list()
    print(f"   {students_list}")
    print(f"   Количество: {len(students_list)}")
    
    # 2. Добавляем студентов
    print("\n2. Добавляем студентов...")
    
    # Студент 1
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate=date(2000, 5, 15),
        group="ИТ-101",
        gpa=4.5
    )
    group.add(student1)
    print(f"   Добавлен: {student1.fio}")
    
    # Студент 2
    student2 = Student(
        fio="Петрова Анна Сергеевна",
        birthdate=date(2001, 3, 20),
        group="ИТ-102",
        gpa=4.8
    )
    group.add(student2)
    print(f"   Добавлен: {student2.fio}")
    
    # Студент 3
    student3 = Student(
        fio="Сидоров Алексей Петрович",
        birthdate=date(1999, 11, 10),
        group="ИТ-101",
        gpa=3.9
    )
    group.add(student3)
    print(f"   Добавлен: {student3.fio}")
    
    # 3. Выводим всех студентов
    print("\n3. Все студенты:")
    all_students = group.list()
    for i, student in enumerate(all_students, 1):
        print(f"   {i}. {student['fio']} | {student['group']} | GPA: {student['gpa']}")
    
    # 4. Тестируем поиск
    print("\n4. Поиск студентов:")
    search_results = group.find("Иванов")
    print(f"   Поиск 'Иванов': {[s['fio'] for s in search_results]}")
    
    search_results = group.find("анна")
    print(f"   Поиск 'анна' (без регистра): {[s['fio'] for s in search_results]}")
    
    # 5. Тестируем обновление
    print("\n5. Обновление студента...")
    updated = group.update("Иванов Иван Иванович", gpa=4.7, group="ИТ-103")
    print(f"   Обновлен Иванов: {updated}")
    print(f"   Новые данные: {group.find('Иванов')[0]}")
    
    # 6. Тестируем статистику
    print("\n6. Статистика группы:")
    stats = group.stats()
    print(f"   Всего студентов: {stats['count']}")
    print(f"   Минимальный GPA: {stats['min_gpa']}")
    print(f"   Максимальный GPA: {stats['max_gpa']}")
    print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"   Распределение по группам: {stats['groups']}")
    print("   Топ-5 студентов:")
    for i, top_student in enumerate(stats['top_5'], 1):
        print(f"     {i}. {top_student['fio']} - GPA: {top_student['gpa']}")
    
    # 7. Тестируем удаление
    print("\n7. Удаление студента...")
    removed = group.remove("Сидоров Алексей Петрович")
    print(f"   Удален Сидоров: {removed}")
    print(f"   Осталось студентов: {len(group.list())}")
    
    # 8. Финальный список
    print("\n8. Финальный список студентов:")
    final_list = group.list()
    for i, student in enumerate(final_list, 1):
        print(f"   {i}. {student['fio']} | {student['group']} | GPA: {student['gpa']}")
    
    print("\n" + "=" * 50)
    print("ТЕСТЫ ЗАВЕРШЕНЫ")
    print("=" * 50)
    
    # Дополнительно: показываем содержимое CSV файла
    print(f"\nСодержимое файла {group.path}:")
    print("-" * 50)
    if group.path.exists():
        with open(group.path, 'r', encoding='utf-8') as f:
            print(f.read())
    print("-" * 50)