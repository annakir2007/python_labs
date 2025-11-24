import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


def test_normalize_basic():
    """Тест базовых случаев нормализации."""
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик елка"  # исправлено!
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"


def test_normalize_edge_cases():
    """Тест граничных случаев нормализации."""
    assert normalize("") == ""
    assert normalize("   ") == ""
    assert normalize("ТЕСТ!") == "тест"  # исправлено!
    assert normalize("раз,два,три") == "раз два три"


def test_tokenize_basic():
    """Тест базовых случаев токенизации."""
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("раз два три") == ["раз", "два", "три"]
    assert tokenize("одно слово") == ["одно", "слово"]


def test_tokenize_edge_cases():
    """Тест граничных случаев токенизации."""
    assert tokenize("") == []
    assert tokenize("   ") == []

    text = "Привет, мир! Как дела?"
    result = tokenize(text)
    expected = ["привет", "мир", "как", "дела"]  # исправлено!
    assert result == expected


def test_count_freq_basic():
    """Тест базовых случаев подсчета частот."""
    tokens = ["я", "ты", "я", "мы", "ты", "я"]
    result = count_freq(tokens)
    expected = {"я": 3, "ты": 2, "мы": 1}
    assert result == expected


def test_count_freq_edge_cases():
    """Тест граничных случаев подсчета частот."""
    assert count_freq([]) == {}

    tokens = ["слово", "слово", "слово"]
    result = count_freq(tokens)
    expected = {"слово": 3}
    assert result == expected


def test_top_n_basic():
    """Тест базовых случаев получения топ-N."""
    freq = {"я": 5, "ты": 3, "мы": 4, "они": 2}
    result = top_n(freq, 3)
    expected = [("я", 5), ("мы", 4), ("ты", 3)]
    assert result == expected


def test_top_n_tie_breaker():
    """Тест сортировки при одинаковых частотах."""
    freq = {"бета": 2, "альфа": 2, "гамма": 2, "дельта": 1}
    result = top_n(freq, 3)
    expected = [("альфа", 2), ("бета", 2), ("гамма", 2)]
    assert result == expected


def test_top_n_edge_cases():
    """Тест граничных случаев получения топ-N."""
    assert top_n({}, 5) == []
    assert top_n({"слово": 1}, 0) == []

    freq = {"а": 1, "б": 2}
    result = top_n(freq, 5)
    expected = [("б", 2), ("а", 1)]
    assert result == expected


def test_full_pipeline():
    """Интеграционный тест всего пайплайна."""
    text = "Раз два три, раз два три. Раз раз раз!"

    normalized = normalize(text)
    assert normalized == "раз два три раз два три раз раз раз"  # исправлено!

    tokens = tokenize(normalized)
    expected_tokens = ["раз", "два", "три", "раз", "два", "три", "раз", "раз", "раз"]
    assert tokens == expected_tokens

    freq = count_freq(tokens)
    expected_freq = {"раз": 5, "два": 2, "три": 2}
    assert freq == expected_freq

    top_words = top_n(freq, 2)
    expected_top = [("раз", 5), ("два", 2)]
    assert top_words == expected_top
