def format_record(rec):
    fio, group, gpa = rec#переменные кортежа

    fio = " ".join(fio.strip().split())#удаляем пробелы в начале и в конце строки фио;разделяем строку по пробелам;объединяем список слов обратно;остались только слова через 1 пробел
    group = group.strip()#Убираем пробелы в начале и конце строки с группой

    if fio == '' or group == '':
        raise ValueError("Пустое ФИО или группа")
    if not isinstance(gpa, (float, int)):
        raise TypeError("ГПА должно быть числом")
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("ФИО должно содержать минимум фамилию и имя")
    surname = parts[0].capitalize()
    initials = "".join([p[0].upper() + "." for p in parts[1:3]])
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

# Примеры
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))