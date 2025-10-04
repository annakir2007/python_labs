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
print(unique_sorted(nums))

def flatten(mat):
    listt = []
    for sublist in mat:
        for item in sublist:
            if not item.isdigit():
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

print(mat)
print(flatten(mat))