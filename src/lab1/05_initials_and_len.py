full_name = input("ФИО: ")
name_parts = full_name.split()
length = len(full_name.replace(" ", "")) + 2
initials = f"{name_parts[0][0]}{name_parts[1][0]}{name_parts[2][0]}."
print(f"Инициалы: {initials}")
print(f"Длина (символов): {length}")
