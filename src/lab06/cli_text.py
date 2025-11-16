import argparse
import sys
import os
from pathlib import Path

sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lib")
from io_helpers import read_file, read_lines, text_analyzer

def cat_command(input_file, number_lines=False):
    """
    Реализация команды cat с нумерацией строк
    """
    lines = read_lines(input_file)#читает файл построчно, возвращает список строк
    
    for i, line in enumerate(lines, 1):
        if number_lines:
            print(f"{i:6}  {line}", end='')
        else:
            print(line, end='')

def stats_command(input_file, top_n=5):
    """
    Реализация команды stats для анализа частот слов
    """
    text = read_file(input_file)#читает весь файл как одну строку
    top_words = text_analyzer(text, top_n)
    
    print(f"Топ-{top_n} самых частых слов в файле '{input_file}':")
    print("-" * 40)
    for i, (word, freq) in enumerate(top_words, 1):#перебирает слова с нумерацией с 1
        print(f"{i:2}. {word:<20} {freq:>3} раз")

def main():
    parser = argparse.ArgumentParser(
        description="CLI утилиты для работы с текстом",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(
        dest="command", 
        help="Доступные команды",
        required=True
    )

    # Подкоманда cat
    cat_parser = subparsers.add_parser(
        "cat", 
        help="Вывести содержимое файла построчно"
    )
    cat_parser.add_argument(
        "--input", 
        required=True,
        help="Путь к входному файлу"
    )
    cat_parser.add_argument(
        "-n", 
        action="store_true",
        help="Нумеровать строки"
    )

    # Подкоманда stats
    stats_parser = subparsers.add_parser(
        "stats", 
        help="Анализ частот слов в тексте"
    )
    stats_parser.add_argument(
        "--input", 
        required=True,
        help="Путь к текстовому файлу"
    )
    stats_parser.add_argument(
        "--top", 
        type=int, 
        default=5,
        help="Количество топ-слов для вывода (по умолчанию: 5)"
    )

    args = parser.parse_args()

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
            
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()