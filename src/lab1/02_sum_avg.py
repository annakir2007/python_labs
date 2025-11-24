a = input("a:")
for i in a:
    if "," in a:
        a = a.replace(",", ".")
a = float(a)

b = input("b:")
for i in b:
    if "," in b:
        b = b.replace(",", ".")
b = float(b)
sum = a + b
avg = sum / 2
print("sum:", sum, ";", "avg:", round(avg, 2))
