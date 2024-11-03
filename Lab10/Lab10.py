import os


# Функція для створення та запису даних у файл
def create_and_write_file(filename):
    try:
        # Отримуємо дані від користувача
        surname = input("Введіть своє прізвище та ім'я: ")
        answer = input("Введіть свою відповідь: ")
        question = input("Введіть питання, на яке має відповісти наступний студент: ")

        # Відкриваємо файл для запису з додаванням нових записів
        with open(filename, 'a') as file:
            # Записуємо прізвище та питання першого студента у файл
            file.write("Прізвище та ім'я: Дмитренко Богдан\n")
            file.write("Питання: Що робить функція print() у Python?\n")

            # Другий студент: Петрушко Ярослав. Відповідь та нове питання.
            file.write(f"Прізвище та ім'я: Петрушко Ярослав\n")
            file.write(
                f"Відповідь: Функція print() виводить вказаний об’єкт на стандартний пристрій виводу (екран) або у файл текстового потоку.\n")
            file.write(
                f"Функція print() може приймати до 5 параметрів: *objects - об'єкт для виводу; sep - роздільник, для декількох об'єктів; end - що виводити в кінці; file - об'єкт із методом запису; flush - скидання виводу (True) чи буферизація (False).\n")
            file.write(f"Питання для наступного студента: Як виконати зріз рядка у Python?\n")

            # Третій студент: Рубан Богдан, відповідь та нове питання
            file.write("Прізвище та ім'я: Рубан Богдан\n")
            file.write(
                "Відповідь: Зріз рядка в Python виконується за допомогою синтаксису рядок[start:stop:step], де start – початкова позиція зрізу (включно), stop – кінцева позиція зрізу (не включно), step – крок, з яким виконується зріз.\n")
            file.write("Приклад:\n")
            file.write("text = 'Python'\n")
            file.write("text[1:4] поверне 'yth', text[:3] поверне 'Pyt', text[::2] поверне 'Pto'.\n")
            file.write("Питання для наступного студента: Як перевернути рядок у Python за допомогою зрізу?\n")

            # Четвертий студент: відповідь та питання
            file.write(f"Прізвище та ім'я: {surname}\n")
            file.write(f"Відповідь: {answer}\n")
            file.write(f"Питання для наступного студента: {question}\n")

        print(f"Файл '{filename}' успішно створено та записано.")

    except OSError as e:
        # Обробка помилки, якщо виникла проблема з файлом
        print(f"Помилка при роботі з файлом: {e}")


# Виклик функції з ім'ям файлу
filename = 'questions_and_answers.txt'
create_and_write_file(filename)
