import models
import serialize

student_list = [
    models.Student('Петр Иванов', '1990-01-01', 'SE-01', 4.0),
    models.Student('Иван Егоров', '1990-01-01', 'SE-110', 3.5),
    models.Student('Иван Иванов', '1990-01-01', 'SE-11', 5.0),
    models.Student('Петр Петров', '1990-01-01', 'SE-02', 2.5),
    models.Student('Иван Егоров', '1990-01-01', 'SE-20', 3.0),
]

print('*** 1) ДЕМО ПЕЧАТИ СТУДЕНТОВ ***')

for index, student_obj in enumerate(student_list):
    print(f'{index+1} студент: {student_obj}')

print('*** 2) ДЕМО СЕРИАЛИЗАЦИИ СТУДЕНТОВ ***')
serialize.students_to_json(student_list, 'students.json')

print('*** 3) ДЕМО ДЕСЕРИАЛИЗАЦИИ СТУДЕНТОВ ***')
loaded_students = serialize.students_from_json('students.json')

for index, student_obj in enumerate(loaded_students):
    print(f'{index+1} студент: {student_obj}')