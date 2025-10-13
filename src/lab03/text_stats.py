import sys
sys.path.append("../lib")
from text import *

text = input()
norm_text = normalize(text)
tokenz = tokenize(norm_text)
freqs = count_freq(tokenz)
top_5 = top_n(freqs, n=5)
print(f"Всего слов: {len(tokenz)}")
print(f"Уникальных слов: {len(freqs.keys())}")
print(f"Топ-5:")
for i in top-5:
    print(f"{i[0]}:{i[1]}")