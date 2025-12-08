import csv
from pathlib import Path
import sys
from datetime import date
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lab08")
from models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)

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