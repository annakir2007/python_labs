import sys
import argparse

sys.path.append(r"C:\Users\Анна\Desktop\misis_proga\python_labs\src\lib")
from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def main():
    # Создаем объект для чтения аргументов командной строки
    parser = argparse.ArgumentParser()

    # Считаем аргументы:
    # --in — входной файл("data/input.txt")
    parser.add_argument("--in", dest="input_file", default="data/input.txt")
    # --out — выходной файл("data/report.csv")
    parser.add_argument("--out", dest="output_file", default="data/report.csv")
    # --encoding — кодировка файла("utf-8")
    parser.add_argument("--encoding", default="utf-8")

    # Распарсиваем аргументы из командной строки
    args = parser.parse_args()

    # Попытка открыть и прочитать входной файл
    try:
        text = read_text(args.input_file)
    except FileNotFoundError:
        print("Файл не найден")
        sys.exit()  # выходим из программы при ошибке

    # Обрабатываем текст: делаем его нормальным и делим на слова
    text = normalize(text)
    tokens = tokenize(text)

    # Подсчитываем, сколько раз каждое слово встречается
    freq = count_freq(tokens)

    # Сортируем слова по количеству встреч
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Создаем таблицу данных для отчета
    header = ["word", "count"]
    data = [[word, count] for word, count in sorted_words]
    # Записываем результат в CSV файл
    write_csv(data, args.output_file, header)

    # Выводим статистику
    total_words = sum(freq.values())  # Общее число всех слов
    unique_words = len(freq)  # Количество уникальных слов
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5 слов:")
    for word, count in top_n(freq, 5):
        print(f"{word} - {count}")


if __name__ == "__main__":
    main()
