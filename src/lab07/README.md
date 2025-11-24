# <h1>ЛР7<h1>

# <h4>test_text.py<h4>

Написала автотесты для всех публичных функций модуля:

normalize(text: str) -> str
tokenize(text: str) -> list[str]
count_freq(tokens: list[str]) -> dict[str, int]
top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]

Вот код к этому заданию:

```
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

```


# <h4>test_json_csv.py<h4>

Написала автотесты для функций:

json_to_csv(src_path: str, dst_path: str)
csv_to_json(src_path: str, dst_path: str)

Вот код к этому заданию:

```
import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    """Тест базовой конвертации JSON в CSV."""
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"

    data = [
        {"name": "Алиса", "age": 25},
        {"name": "Боб", "age": 30},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    assert dst.exists()

    with dst.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert rows[0]["name"] == "Алиса"
    assert rows[0]["age"] == "25"
    assert rows[1]["name"] == "Боб"
    assert rows[1]["age"] == "30"


def test_json_to_csv_missing_fields(tmp_path):
    """Тест с отсутствующими полями."""
    src = tmp_path / "test.json"
    dst = tmp_path / "test.csv"

    data = [
        {"name": "Алиса", "age": 25},
        {"name": "Боб", "city": "Москва"},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age", "city"}
    assert rows[0]["name"] == "Алиса"
    assert rows[0]["city"] == ""
    assert rows[1]["age"] == ""


def test_json_to_csv_file_not_found():
    """Тест с несуществующим файлом."""
    with pytest.raises(FileNotFoundError):
        json_to_csv("nonexistent.json", "output.csv")


def test_json_to_csv_invalid_json(tmp_path):
    """Тест с некорректным JSON."""
    src = tmp_path / "invalid.json"
    dst = tmp_path / "output.csv"

    src.write_text("{ invalid json }", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_empty_json(tmp_path):
    """Тест с пустым JSON."""
    src = tmp_path / "empty.json"
    dst = tmp_path / "output.csv"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_basic(tmp_path):
    """Тест базовой конвертации CSV в JSON."""
    src = tmp_path / "test.csv"
    dst = tmp_path / "test.json"

    csv_content = """name,age,city
Алиса,25,Москва
Боб,30,СПб"""

    src.write_text(csv_content, encoding="utf-8")
    csv_to_json(str(src), str(dst))

    assert dst.exists()

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0] == {"name": "Алиса", "age": "25", "city": "Москва"}
    assert data[1] == {"name": "Боб", "age": "30", "city": "СПб"}


def test_csv_to_json_file_not_found():
    """Тест с несуществующим файлом."""
    with pytest.raises(FileNotFoundError):
        csv_to_json("nonexistent.csv", "output.json")


def test_csv_to_json_empty_csv(tmp_path):
    """Тест с пустым CSV."""
    src = tmp_path / "empty.csv"
    dst = tmp_path / "output.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst))


def test_round_trip(tmp_path):
    """Тест круговой конвертации JSON->CSV->JSON."""
    original_json = tmp_path / "original.json"
    intermediate_csv = tmp_path / "intermediate.csv"
    final_json = tmp_path / "final.json"

    original_data = [
        {"name": "Алиса", "age": 25},
        {"name": "Боб", "age": 30},
    ]

    original_json.write_text(
        json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
    )

    json_to_csv(str(original_json), str(intermediate_csv))
    csv_to_json(str(intermediate_csv), str(final_json))

    with final_json.open(encoding="utf-8") as f:
        final_data = json.load(f)

    assert len(final_data) == len(original_data)

```


![](./images/lb06/img_1.png)


![](./images/lb06/img_2.png)
