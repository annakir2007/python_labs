def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # Заменяем управляющие символы \r, \n, \t на пробелы
    text = text.replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')

    # Замена ё/Ё на е/Е
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    # Применение casefold (если требуется) с обработкой ошибок
    '''Если мы хотим делать все буквы маленькими, то сначала пытаемся использовать casefold(), которая очень хорошо переводит все буквы в маленькие и делает слова одинаковыми.
Если casefold() не работает, тогда используем lower() — тоже превращает буквы в маленькие.'''
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
            if not prev_space:#если не пробел --> True
                result_chars.append(' ')
                prev_space = True
        else:
            result_chars.append(ch)#не является пробелом, значит добавляем текущий символ ch в итоговый список.
            prev_space = False#обнуляем флаг
    normalized_text = ''.join(result_chars).strip()#удаление лишних пробелов с начала и с конца
    #Объединяем список символов result_chars в строку.
    return normalized_text


def tokenize(text: str) -> list[str]:
    tokens = []#список хранения итоговых токенов
    current_word = []#список символов текущего слова

    def is_word_char(c):#возвращает True, если символ - буква, цифра, подчёркивание или дефис
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
                tokens.append(''.join(current_word))#Объединяет символы в строку и добавляет в список tokens
                current_word = []#сброс списка для следующего слова
    #После завершения цикла, если есть ещё незанесённое слово, добавляем его.
    if current_word:
        tokens.append(''.join(current_word))
    return tokens

#для каждого токена увеличивает значение по ключу token на 1
def count_freq(tokens: list[str]) -> dict:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq#словарь, где ключ — токен, значение — количество



#сортирует пары в словаре по убыванию частоты(-item[1])(если равны, по алфавиту(item[0])); возвращает первые n элементов из отсортированного списка
def top_n(freq: dict, n: int = 5) -> list:
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]

#тесты

# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]