import csv
import json
import os

# Дмитреноко Богдан create_csv, csv_to_json

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

    # Запис даних у JSON файл з фігурними дужками
    try:
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump({"students": data}, json_file, indent=4)
        print(f"JSON файл '{json_filename}' успішно створено.")
    except Exception as e:
        print(f"Помилка при записі JSON файлу: {e}")

# Рубан Богдан JSON_TO_CSV
def json_to_csv(json_filename, csv_filename):
    """Конвертує дані з .json у .csv файл, додаючи нові рядки."""
    new_data = [
        {"id": "4", "name": "Anastasia", "age": "22"},
        {"id": "5", "name": "Ilya", "age": "21"},
    ]

    # Читання даних з JSON
    try:
        with open(json_filename, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)["students"]  # Доступ до списку студентів
        print(f"Дані успішно зчитано з '{json_filename}'.")
    except FileNotFoundError:
        print(f"Файл '{json_filename}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні JSON файлу: {e}")
        return

    # Запис даних у новий CSV файл
    try:
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "name", "age"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)  # Существующие дані з JSON
            writer.writerows(new_data)  # Нові дані
        print(f"CSV файл '{csv_filename}' успішно створено з новими рядками.")
    except Exception as e:
        print(f"Помилка при записі нового CSV файлу: {e}")

# Петрушко Ярослав csv_to_json
def csv_to_json_updated(csv_filename, json_filename):
    """Переписує дані з .csv у .json файл, додаючи нові рядки."""
    
    # Додаткові дані для запису
    new_data = [
        {"id": "6", "name": "Roman", "age": "20"},
        {"id": "7", "name": "Denis", "age": "19"}
    ]

    # Структура для запису в JSON з ключем "students"
    json_data = {"students": []}

    # Зчитуємо дані з CSV файлу та додаємо їх у JSON структуру
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            json_data["students"].extend(reader)
        print(f"Дані успішно зчитано з '{csv_filename}'.")
    except FileNotFoundError:
        print(f"Файл '{csv_filename}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні CSV файлу: {e}")
        return

    # Додаємо нові дані
    json_data["students"].extend(new_data)
    
    # Записуємо всю структуру у JSON файл
    try:
        with open(json_filename, mode='w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON файл '{json_filename}' успішно створено з новими рядками.")
    except Exception as e:
        print(f"Помилка при записі JSON файлу: {e}")


# Шляхи до файлів
csv_filename = "students.csv"
json_filename = "students.json"
new_csv_filename = "students_updated.csv"
new_json_filename = "students_updated.json"

# Виконання функцій
create_csv(csv_filename)
csv_to_json(csv_filename, json_filename)
json_to_csv(json_filename, new_csv_filename)
csv_to_json_updated(new_csv_filename, new_json_filename)



