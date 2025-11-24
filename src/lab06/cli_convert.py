import argparse
import sys
import os
from pathlib import Path

sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lab05")
from json_csv import json_to_csv, csv_to_json
from csv_xlsx import csv_to_xlsx


def json2csv_command(args):
    """Обработка команды json2csv"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        json_to_csv(args.input, args.output)
        print(f"Успешно конвертировано: {args.input} -> {args.output}")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def csv2json_command(args):
    """Обработка команды csv2json"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        csv_to_json(args.input, args.output)
        print(f"Успешно конвертировано: {args.input} -> {args.output}")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def csv2xlsx_command(args):
    """Обработка команды csv2xlsx"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        csv_to_xlsx(args.input, args.output)
        print(f"Успешно конвертировано: {args.input} -> {args.output}")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI-конвертеры данных между форматами JSON, CSV и XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python -m src.lab06.cli_convert json2csv --in data.json --out data.csv
  python -m src.lab06.cli_convert csv2json --in data.csv --out data.json
  python -m src.lab06.cli_convert csv2xlsx --in data.csv --out data.xlsx

        """,
    )

    subparsers = parser.add_subparsers(
        dest="command", help="Доступные команды конвертации", required=True
    )

    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON файл"
    )
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV файл"
    )
    json2csv_parser.set_defaults(func=json2csv_command)

    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON файл"
    )
    csv2json_parser.set_defaults(func=csv2json_command)

    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX файл"
    )
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
