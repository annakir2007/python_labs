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
    listt = []
    for sublist in mat:#внутренние списки
        for item in sublist:#по элементам
            if not item.isdigit():#проверка на все числа
                return 'TypeError'
            else:
                listt.append(int(item))
    return listt

n = int(input("Сколько списков вы хотите создать? "))
mat = []
for i in range(n):
    elements = input(f"Введите числа для списка {i + 1} через пробел: ")
    inner_list = elements.split()
    mat.append(inner_list)

print(min_max(nums))
print(unique_sorted(nums))
print(flatten(mat))