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
