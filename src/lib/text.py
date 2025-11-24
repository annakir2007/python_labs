import re
from collections import Counter


def normalize(text: str) -> str:
    """Приводит текст к нижнему регистру и удаляет лишние пробелы."""
    if not text:
        return ""

    # Приводим к нижнему регистру
    text = text.lower()

    # Заменяем букву ё на е
    text = text.replace("ё", "е")

    # Заменяем все не-буквенные и не-пробельные символы на пробелы
    text = re.sub(r"[^a-zа-я\s]", " ", text)

    # Заменяем множественные пробелы на один
    text = re.sub(r"\s+", " ", text)

    # Убираем пробелы в начале и конце
    return text.strip()


def tokenize(text: str) -> list[str]:
    """Разбивает текст на слова (токены)."""
    if not text:
        return []

    normalized = normalize(text)
    return normalized.split() if normalized else []


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитывает частоту встречаемости каждого токена."""
    return dict(Counter(tokens))


def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Возвращает n самых частых токенов с их частотами."""
    if not freq or n <= 0:
        return []

    # Сортируем по убыванию частоты, при равенстве - по алфавиту
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[:n]
