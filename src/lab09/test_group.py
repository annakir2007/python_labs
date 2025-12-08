# test_group_manager.py
from datetime import date
from group import Group
import sys
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lab08")
from models import Student

class StudentManager:
    def __init__(self, file_path):
        self.group = Group(file_path)
    
    def list_all(self):
        """Выводит список всех студентов"""
        students = self.group.list()
        
        if not students:
            print("В базе нет записей")
            return
        
        print("\n" + "=" * 80)
        print(f"{'№':3} | {'ФИО':30} | {'Группа':8} | {'Дата рождения':12} | {'GPA':5}")
        print("=" * 80)
        
        for i, student in enumerate(students, 1):
            print(f"{i:3} | {student['fio']:30} | {student['group']:8} | "
                  f"{student['birthdate']:12} | {student['gpa']:5}")
        print(f"\nВсего студентов: {len(students)}")
    
    def add_student(self):
        """Добавляет нового студента"""
        print("\n" + "=" * 50)
        print("Добавление нового студента")
        print("=" * 50)
        
        # Ввод данных
        fio = input("Введите ФИО студента: ").strip()
        if not fio:
            print("ФИО не может быть пустым!")
            return
        
        birthdate_str = input("Введите дату рождения (ГГГГ-ММ-ДД): ").strip()
        # Проверка и преобразование даты
        try:
            year, month, day = map(int, birthdate_str.split('-'))
            birthdate = date(year, month, day)
        except (ValueError, AttributeError):
            print("Неверный формат даты! Используйте ГГГГ-ММ-ДД")
            return
        
        group = input("Введите группу: ").strip()
        if not group:
            print("Группа не может быть пустой!")
            return
        
        try:
            gpa = float(input("Введите средний балл (GPA): ").strip())
            if not 0 <= gpa <= 5:
                print("GPA должен быть от 0 до 5!")
                return
        except ValueError:
            print("GPA должен быть числом!")
            return
        
        # Проверяем, нет ли уже такого студента
        existing = self.group.find(fio)
        if existing:
            print(f"Студент с ФИО '{fio}' уже существует!")
            return
        
        # Создаем объект Student и добавляем
        try:
            student = Student(fio=fio, birthdate=birthdate, group=group, gpa=gpa)
            self.group.add(student)
            print(f"\nСтудент '{fio}' успешно добавлен!")
        except Exception as e:
            print(f"\nОшибка при добавлении студента: {e}")
    
    def remove_student(self):
        """Удаляет студента"""
        print("\n" + "=" * 50)
        print("Удаление студента")
        print("=" * 50)
        
        students = self.group.list()
        
        if not students:
            print("В базе нет записей для удаления")
            return
        
        # Показываем список для выбора
        print("Текущие студенты:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['fio']}")
        
        choice = input("\nВведите номер студента для удаления или ФИО: ").strip()
        
        try:
            # Если ввели номер
            index = int(choice) - 1
            if 0 <= index < len(students):
                fio = students[index]['fio']
            else:
                print("Неверный номер!")
                return
        except ValueError:
            # Если ввели ФИО
            fio = choice
        
        # Подтверждение
        confirm = input(f"Удалить студента '{fio}'? (да/нет): ").strip().lower()
        if confirm not in ['да', 'д', 'yes', 'y']:
            print("Удаление отменено")
            return
        
        # Удаляем через метод Group
        if self.group.remove(fio):
            print(f"\nСтудент '{fio}' успешно удален!")
        else:
            print(f"\nСтудент с ФИО '{fio}' не найден!")
    
    def update_student(self):
        """Обновляет данные студента"""
        print("\n" + "=" * 50)
        print("Обновление данных студента")
        print("=" * 50)
        
        students = self.group.list()
        
        if not students:
            print("В базе нет записей для обновления")
            return
        
        # Показываем список для выбора
        print("Текущие студенты:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['fio']} - {student['group']} - GPA: {student['gpa']}")
        
        choice = input("\nВведите номер студента для обновления или ФИО: ").strip()
        
        try:
            # Если ввели номер
            index = int(choice) - 1
            if 0 <= index < len(students):
                student = students[index]
                fio = student['fio']
            else:
                print("Неверный номер!")
                return
        except ValueError:
            # Если ввели ФИО
            fio = choice
            # Ищем студента
            found = False
            for s in students:
                if s['fio'].lower() == fio.lower():
                    student = s
                    found = True
                    break
            
            if not found:
                print(f"Студент с ФИО '{fio}' не найден!")
                return
        
        print(f"\nРедактирование студента: {fio}")
        print("(Оставьте поле пустым, чтобы не изменять)")
        
        # Собираем обновления
        updates = {}
        
        new_fio = input(f"Новое ФИО [{student['fio']}]: ").strip()
        if new_fio:
            updates['fio'] = new_fio
        
        new_birthdate = input(f"Новая дата рождения [{student['birthdate']}]: ").strip()
        if new_birthdate:
            try:
                year, month, day = map(int, new_birthdate.split('-'))
                updates['birthdate'] = date(year, month, day)
            except (ValueError, AttributeError):
                print("Неверный формат даты! Используйте ГГГГ-ММ-ДД")
                return
        
        new_group = input(f"Новая группа [{student['group']}]: ").strip()
        if new_group:
            updates['group'] = new_group
        
        new_gpa = input(f"Новый GPA [{student['gpa']}]: ").strip()
        if new_gpa:
            try:
                gpa_value = float(new_gpa)
                if 0 <= gpa_value <= 5:
                    updates['gpa'] = gpa_value
                else:
                    print("GPA должен быть от 0 до 5!")
                    return
            except ValueError:
                print("GPA должен быть числом!")
                return
        
        # Если есть обновления, применяем их
        if updates:
            if self.group.update(fio, **updates):
                print(f"\nДанные студента успешно обновлены!")
            else:
                print(f"\nОшибка при обновлении данных студента!")
        else:
            print("Нет изменений для сохранения")
    
    def search_student(self):
        """Ищет студентов по фамилии"""
        print("\n" + "=" * 50)
        print("Поиск студента")
        print("=" * 50)
        
        search_term = input("Введите фамилию или часть ФИО для поиска: ").strip()
        
        if not search_term:
            print("Введите текст для поиска!")
            return
        
        found_students = self.group.find(search_term)
        
        if found_students:
            print(f"\nНайдено студентов: {len(found_students)}")
            print("-" * 70)
            print(f"{'ФИО':30} | {'Группа':8} | {'Дата рождения':12} | {'GPA':5}")
            print("-" * 70)
            
            for student in found_students:
                print(f"{student['fio']:30} | {student['group']:8} | "
                      f"{student['birthdate']:12} | {student['gpa']:5}")
        else:
            print(f"Студенты по запросу '{search_term}' не найдены")
    
    def show_statistics(self):
        """Показывает статистику"""
        print("\n" + "=" * 50)
        print("Статистика")
        print("=" * 50)
        
        stats = self.group.stats()
        
        if stats['count'] == 0:
            print("В базе нет записей для статистики")
            return
        
        print(f"Общее количество студентов: {stats['count']}")
        print(f"Средний GPA: {stats['avg_gpa']:.2f}")
        print(f"Минимальный GPA: {stats['min_gpa']}")
        print(f"Максимальный GPA: {stats['max_gpa']}")
        
        if stats['groups']:
            print(f"\nРаспределение по группам:")
            for group, count in sorted(stats['groups'].items()):
                print(f"  {group}: {count} студент(ов)")
        
        if stats['top_5']:
            print(f"\nТоп-5 студентов по GPA:")
            for i, student in enumerate(stats['top_5'], 1):
                print(f"  {i}. {student['fio']}: {student['gpa']}")

def main():
    """Главная функция с меню"""
    # Путь к файлу
    file_path = r"C:\Users\Анна\Desktop\misis_proga\python_labs\data\lab09\students.csv"
    
    # Создаем менеджер
    manager = StudentManager(file_path)
    
    while True:
        print("\n" + "=" * 50)
        print("Управление базой данных студентов")
        print("Используется класс Group из group.py")
        print("=" * 50)
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Удалить студента")
        print("4. Обновить данные студента")
        print("5. Поиск по фамилии")
        print("6. Показать статистику")
        print("7. Проверить существование файла")
        print("8. Выход")
        print("=" * 50)
        
        choice = input("Выберите действие (1-8): ").strip()
        
        if choice == "1":
            manager.list_all()
        elif choice == "2":
            manager.add_student()
        elif choice == "3":
            manager.remove_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            manager.show_statistics()
        elif choice == "7":
            print(f"\nПроверка файла:")
            print(f"Путь: {manager.group.path}")
            print(f"Файл существует: {manager.group.path.exists()}")
            print(f"Количество студентов: {len(manager.group.list())}")
        elif choice == "8":
            print("Выход...")
            break
        else:
            print("Неверный выбор! Введите число от 1 до 8")
        
        input("\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    main()