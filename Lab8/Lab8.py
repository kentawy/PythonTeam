# Дмитренко Богдан, написання словнику, написання 2 функцій Додавання + Виведення списку

# Ініціалізуємо порожній словник для зберігання даних про студентів
student_performance = {}


# Функція для додавання даних про студента
def add_student(group_number, full_name, course, subjects_grades):
    """
    Додає дані про студента в словник.

    Parameters:
        group_number (str): Номер групи студента.
        full_name (str): Прізвище, ім'я, по батькові студента.
        course (int): Курс студента.
        subjects_grades (dict): Оцінки студента по предметах у форматі {предмет: оцінка}.
    """
    student_performance[full_name] = {
        'group_number': group_number,
        'course': course,
        'subjects_grades': subjects_grades
    }
    print(f"Студента {full_name} додано успішно.")


# Функція для форматованого виведення даних про студентів
def display_students():
    """
    Виводить інформацію про всіх студентів у форматованому вигляді.
    """
    if not student_performance:
        print("Список студентів порожній.")
    else:
        for name, details in student_performance.items():
            print(f"Студент: {name}")
            print(f"  Група: {details['group_number']}")
            print(f"  Курс: {details['course']}")
            print("  Оцінки:")
            for subject, grade in details['subjects_grades'].items():
                print(f"    {subject}: {grade}")
            print("-" * 40)  # роздільник між студентами


# Функція для обробки вибору користувача
def handle_action(action):
    """
    Обробляє дію користувача через switch-case (імітація за допомогою словника функцій).

    Parameters:
        action (str): Дія, яку потрібно виконати ("add" або "display").
    """
    actions = {
        "add": add_student_prompt,
        "display": display_students
    }

    # Виконуємо функцію, якщо вона існує у словнику
    if action in actions:
        actions[action]()
    else:
        print("Невідома команда! Доступні команди: 'add', 'display'.")


# Функція для взаємодії з користувачем і додавання студента через запити
def add_student_prompt():
    """
    Запитує у користувача дані для нового студента і додає його в словник.
    """
    group_number = input("Введіть номер групи: ")
    full_name = input("Введіть ПІБ студента: ")
    course = int(input("Введіть курс студента: "))

    # Запитуємо предмети та оцінки
    subjects_grades = {}
    print("Введіть предмети та оцінки студента (для завершення введіть 'завершити'): ")
    while True:
        subject = input("Предмет: ")
        if subject.lower() == 'завершити':
            break
        grade = int(input(f"Оцінка для {subject}: "))
        subjects_grades[subject] = grade

    add_student(group_number, full_name, course, subjects_grades)
add_student('КН-37-4', 'Дмитренко Богдан', 2, {'Чисельні методи': 90, 'ММДО': 85, 'Algorithms and Data Structures': 95})
add_student('КН-37-4', 'Петрушко Ярослав', 3, {'Математика': 75, 'Фізика': 80, 'Інформатика': 88})
add_student('КН-37-4', 'Рубан Богдан', 2, {'Чисельні методи': 90, 'ММДО': 85, 'Algorithms and Data Structures': 95})
add_student('КН-37-4', 'Гаценко Максим', 2, {'Чисельні методи': 90, 'ММДО': 85, 'Algorithms and Data Structures': 95})
add_student('КН-37-4', 'Лукянченко Сергій', 2, {'Чисельні методи': 90, 'ММДО': 85, 'Algorithms and Data Structures': 95})

# Основний цикл програми
while True:
    print("\nКоманди: 'add' - додати студента, 'display' - показати список студентів, 'exit' - вихід")
    action = input("Введіть команду: ").strip().lower()
    if action == "exit":
        print("Програма завершена.")
        break
    handle_action(action)
