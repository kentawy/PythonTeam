import csv
import json
import os


def create_csv(filename):
    """Створює .csv файл із початковими даними."""
    data = [
        {"id": "1", "name": "Bogdan", "age": "19"},
        {"id": "2", "name": "Yaroslav", "age": "20"},
        {"id": "3", "name": "Maksim", "age": "18"},
    ]

    # Створення CSV файлу
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "name", "age"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV файл '{filename}' успішно створено.")
    except Exception as e:
        print(f"Помилка при створенні CSV файлу: {e}")


def csv_to_json(csv_filename, json_filename):
    """Конвертує дані з .csv у .json файл."""
    data = []

    # Читання даних з CSV
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)
        print(f"Дані успішно зчитано з '{csv_filename}'.")
    except FileNotFoundError:
        print(f"Файл '{csv_filename}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні CSV файлу: {e}")
        return

    # Запис даних у JSON файл
    try:
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON файл '{json_filename}' успішно створено.")
    except Exception as e:
        print(f"Помилка при записі JSON файлу: {e}")


# Шляхи до файлів
csv_filename = "students.csv"
json_filename = "students.json"

# Виконання функцій
create_csv(csv_filename)
csv_to_json(csv_filename, json_filename)
