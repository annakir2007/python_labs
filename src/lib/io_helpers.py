import os
import json
import csv
from pathlib import Path

def read_file(file_path):
    """Чтение файла с проверкой существования"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_lines(file_path):
    """Чтение файла построчно"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_file(file_path, content):
    """Запись в файл с созданием директорий при необходимости"""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def ensure_directory(file_path):
    """Создание директории для файла если не существует"""
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)