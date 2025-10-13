def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # Заменяем управляющие символы \r, \n, \t на пробелы
    text = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

    # Замена ё/Ё на е/Е
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    # Применение casefold (если требуется) с обработкой ошибок
    '''Если мы хотим делать все буквы маленькими, то сначала пытаемся использовать casefold(), которая очень хорошо переводит все буквы в маленькие и делает слова одинаковыми.
Если вдруг у нас очень старый Python, и casefold() не работает, тогда используем lower() — тоже превращает буквы в маленькие.'''
    if casefold:
        try:
            text = text.casefold()
        except AttributeError:
            text = text.lower()

    # Схлопываем подряд идущие пробелы в один и удаляем пробелы по краям
    result_chars = []#сюда будем добавлять буквы
    prev_space = False#флажок, который говорит, был ли предыдущий символ пробелом.
    for ch in text:
        if ch.isspace():#Если символ — это пробел или похожий знак (isspace() значит — пробел, табуляция или перевод строки),
            if not prev_space:
                result_chars.append(' ')
                prev_space = True
        else:
            result_chars.append(ch)
            prev_space = False
    normalized_text = ''.join(result_chars).strip()
    return normalized_text


def tokenize(text: str) -> list[str]:
    tokens = []
    current_word = []

    def is_word_char(c):
        return c.isalnum() or c in ['_', '-']

    for c in text:
        if is_word_char(c):
            current_word.append(c)
        elif c == '-':
            # дефис внутри слова — добавляем, если слово уже есть
            if current_word:
                current_word.append(c)
        else:
            # разделитель
            if current_word:
                tokens.append(''.join(current_word))
                current_word = []
    if current_word:
        tokens.append(''.join(current_word))
    return tokens


def count_freq(tokens: list[str]) -> dict:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict, n: int = 5) -> list:
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

#тесты

text = "ПрИвЕт\nМИр\t"
text1 = 'ёжик, Ёлка'
text2 = 'Hello\r\nWorld'
text3 = '  двойные  пробелы  '
norm = normalize(text)
norm1 = normalize(text1)
norm2 = normalize(text2)
norm3 = normalize(text3)
print(norm)  
print(norm1)
print(norm2)
print(norm3)


stroka = 'привет мир'
stroka1 = 'hello,world!!!'
stroka2 = 'по-настоящему круто'
stroka3 = '2025 год'
stroka4 = 'emoji 😃 не слово'

tokens = tokenize(stroka)
tokens1 = tokenize(stroka1)
tokens2 = tokenize(stroka2)
tokens3 = tokenize(stroka3)
tokens4 = tokenize(stroka4)
print(tokens) 
print(tokens1)
print(tokens2)
print(tokens3)
print(tokens4)

test = ['a', 'b', 'a', 'c', 'b', 'a']
test1 = ['bb', 'aa', 'bb', 'aa', 'cc']
freq = count_freq(test)
print(freq)

freq1 = count_freq(test1)
top = top_n(freq1)
print(top)