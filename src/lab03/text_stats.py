import sys
sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lib")
from text import normalize, tokenize, count_freq, top_n

text = input()
norm_txt = normalize(text)
token = tokenize(norm_txt)
freq = count_freq(token)#создает словарь, где ключ — слово, значение — сколько раз оно встречается.
top_5 = top_n(freq, n=5)#получает список из 5 наиболее часто встречающихся слов.
print(f"Всего слов: {len(token)}")
print(f"Уникальных слов: {len(freq.keys())}")# длина всех ключей в словаре
print(f"Топ-5:")
for i in top_5:
    print(f"{i[0]}:{i[1]}")