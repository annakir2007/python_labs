nums = []
n = int(input())
for i in range(n):
    s = input()
    if '.' in s:
        number = float(s)
    else:
        number = int(s)
    nums.append(number)
print(nums)

def min_max(nums):
    if len(nums) == 0:
        return "ValueError"
    return (min(nums), int(max(nums)))

def unique_sorted(nums):
    return sorted(set(nums))

def flatten(mat):
    # Если вход - кортеж, преобразуем его в список
    if isinstance(mat, tuple):
        mat = list(mat)

    listt = []
    for sublist in mat:  # могут быть и списки, и кортежи
        # Определяем возможные вложенные кортежи/списки
        if isinstance(sublist, (list, tuple)):
            for item in sublist:
                # Проверка, является ли item числом или строкой
                if isinstance(item, str):#если элемент - строка
                    if not item.isdigit():
                        return 'TypeError'
                    else:
                        listt.append(int(item))
                elif isinstance(item, (int, float)):#если элемент - число
                    listt.append(item)
                else:
                    return 'TypeError'
        else:
            # Если внутри не список/кортеж, возможно, ошибка
            return 'TypeError'
    return listt

n = int(input("Сколько списков вы хотите создать? "))
mat = []
for i in range(n):
    elements = input(f"Введите числа для списка {i + 1} через пробел: ")
    inner_list = elements.split()
    mat.append(inner_list)
print(flatten([(1, 2), (3, 4)]))
print(flatten([[1, 2], [3, 4]]))
print(min_max(nums))
print(unique_sorted(nums))
print(flatten(mat))