# Програмний код написанав  Дмитренко Богдан


import os

# Функція для створення та запису даних у файл
def create_and_write_file(filename):
    try:
        # Отримуємо дані від користувача
        surname = input("Введіть своє прізвище та ім'я: ")
        answer = input("Введіть свою відповідь: ")
        question = input("Введіть питання, на яке має відповісти наступний студент: ")

        # Відкриваємо файл для запису
        with open(filename, 'w') as file:
            # Записуємо прізвище та питання у файл
            file.write("Прізвище: Дмитренко Богдан\n")
            file.write("Питання: Що робить функція print() у Python?\n")
            # Питання Дмитренко Богдана
            file.write(f"Прізвище та ім'я: {surname}\n")
            file.write(f"Відповідь: {answer}\n")
            file.write(f"Питання: {question}\n")
        print(f"Файл '{filename}' створено та записано успішно.")
    except OSError as e:
        # Обробка помилки, якщо виникла проблема з файлом
        print(f"Помилка при роботі з файлом: {e}")

# Виклик функції з ім’ям файлу
filename = 'questions_and_answers.txt'
create_and_write_file(filename)

