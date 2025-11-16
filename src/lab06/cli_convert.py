#!/usr/bin/env python3
"""
CLI конвертеры данных между форматами JSON, CSV и XLSX
Использует функции из lab05 для конвертации
"""

# ИМПОРТЫ ИЗ LAB05 - как требует ТЗ
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

import argparse
import sys
import os
from pathlib import Path

# Добавляем путь для импорта модулей
current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.insert(0, str(project_root))

def json2csv_command(args):
    """Обработка команды json2csv с использованием функции из lab05"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        
        # ИСПОЛЬЗУЕМ ФУНКЦИЮ ИЗ LAB05
        json_to_csv(args.input, args.output)
        print(f"Успешно конвертировано: {args.input} -> {args.output}")
        
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def csv2json_command(args):
    """Обработка команды csv2json с использованием функции из lab05"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        
        # ИСПОЛЬЗУЕМ ФУНКЦИЮ ИЗ LAB05
        csv_to_json(args.input, args.output)
        print(f"Успешно конвертировано: {args.input} -> {args.output}")
        
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

def csv2xlsx_command(args):
    """Обработка команды csv2xlsx с использованием функции из lab05"""
    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")
        
        # ИСПОЛЬЗУЕМ ФУНКЦИЮ ИЗ LAB05
        csv_to_xlsx(args.input, args.output)
        print(f"Упрощенная конвертация: {args.input} -> {args.output}")
        print("💡 Примечание: для полной поддержки XLSX установите библиотеку openpyxl")
        
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
  
Использует функции конвертации из лабораторной работы №5.
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды конвертации", required=True)
    
    # Подкоманда json2csv
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    json2csv_parser.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    json2csv_parser.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")
    json2csv_parser.set_defaults(func=json2csv_command)
    
    # Подкоманда csv2json
    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2json_parser.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")
    csv2json_parser.set_defaults(func=csv2json_command)
    
    # Подкоманда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    csv2xlsx_parser.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()