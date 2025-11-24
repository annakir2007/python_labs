def format_record(rec):
    # Проверка, что rec — кортеж
    if not isinstance(rec, tuple):
        raise TypeError("Аргумент должен быть кортежем")

    if len(rec) != 3:
        raise ValueError("Кортеж должен содержать ровно 3 элемента: (fio, group, gpa)")

    fio, group, gpa = rec

    # Проверка типов для каждого элемента
    if not isinstance(fio, str):
        raise TypeError("fio должен быть строкой")
    if not isinstance(group, str):
        raise TypeError("group должен быть строкой")
    if not isinstance(gpa, (float, int)):
        raise TypeError("gpa должно быть числом (float или int)")

    # Проверка на пустую строку для fio и group
    fio = " ".join(fio.strip().split())
    group = group.strip()

    if fio == "" or group == "":
        raise ValueError("fio и group не должны быть пустыми строками")

    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать минимум фамилию и имя")

    surname = parts[0].capitalize()
    initials = "".join([p[0].upper() + "." for p in parts[1:3]])
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


# Примеры тестов
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))

# Дополнительные тесты с ошибками:
# print(format_record(["Иванов Иван Иванович", "BIVT-25", 4.6]))  # не кортеж
# print(format_record(("Иванов Иван Иванович", "BIVT-25", "4.6")))  # gpa не число
# print(format_record(("Иванов Иван Иванович", "", 4.6)))           # пустая group
# print(format_record(("", "BIVT-25", 4.6)))                       # пустое fio
