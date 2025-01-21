import random
from datetime import datetime, timedelta
from colorama import Fore, Back
from utils import tuple_keys

# Перевод строки в дату, если строка дана в одном из 6 форматов.
def create_date (str_date):
    formated_date = ""
    formate_list = []
    date_formats = ("%Y-%m-%d", "%Y-%d-%m", "%m-%d-%Y", "%m-%Y-%d", "%d-%m-%Y", "%d-%Y-%m")
    for i in date_formats:
        try:
            datetime.strptime(str_date, i).date()
            formate_list.append(i)
        except ValueError:
            pass
    if not formate_list:
        print(Fore.LIGHTRED_EX + "Дата задачи введена некорректно! Повторите ввод.")
        return None
    elif len(formate_list) == 1:
        return datetime.strptime(str_date, formate_list[0]).date()
    elif len(formate_list) > 1:
        while True:
            print()
            print(Fore.LIGHTYELLOW_EX + "Подходит несколько вариантов формата даты. Выберите один из списка ниже:")
            for i in range(len(formate_list)):
                print(f"[{i}]: {formate_list[i]}")
            try:
                key = int(input(Fore.LIGHTYELLOW_EX + "Введите цифру из списка выше."))
            except ValueError:
                print(Fore.LIGHTRED_EX + "Требуется ввести цифру из списка выше.")
                continue
            if key in range((len(formate_list))):
                return datetime.strptime(str_date, formate_list[key]).date()

# Сравнение даты + возврат даты.
def get_date (word, date = None, issue_date = datetime.strptime("3000-01-01", "%Y-%m-%d").date()):
    date_today = datetime.today().date()
    print(Fore.LIGHTYELLOW_EX + f"Введите дату {word} задачи через дефис, например 31-12-2024:")
    if word.capitalize() == "Начала":
        output = "Если введена пустая строка, то дата " + word + " будет равна текущей дате."
    elif word.capitalize() == "Конца":
        output = "Если введена пустая строка, то дата " + word + " будет равна неделе спустя, от текущей даты."
    else:
        print("Некорректный ввод!")
        return date_today
    str_date = input(output)

    # Проверка на пустую строку и сразу возврат.
    # Если начало заметки - сегодня, если окончание - через неделю.
    if str_date == "":
        if word.capitalize() == "Начала":
            print(Fore.LIGHTGREEN_EX + "Дата начала заметки установлена на сегодня.")
            return date_today
        else:
            print(Fore.LIGHTGREEN_EX + "Дата истечения заметки установлена через 7 дней.")
            return date_today + timedelta(7)

    # Если не пустая строка, то
    formated_date = create_date(str_date)
    while formated_date is None:
        formated_date = create_date(input(Fore.LIGHTYELLOW_EX + f"Введите дату {word} задачи через дефис, например 31-12-2024:"))

    # Дата начала меньше даты истечения. (Проверка)
    if word.capitalize() == "Начала":
        if formated_date > issue_date:
            print(Fore.LIGHTRED_EX + "Введенная дата начала больше, чем дата истечения. Изменения не внесены.")
            return date
    return formated_date

#Ввод статуса заявки из списка, остальные статусы отбрасываются.
def get_status():
    tuple_status = ("Новая", "В процессе", "Отложено", "Выполнено", "Отменено")
    while True:
        print(Fore.LIGHTYELLOW_EX + "\nВведите статус из списка ниже. Вы можете ввести его полностью или указать число.")
        print(Fore.LIGHTWHITE_EX + "Список статусов:")
        for i in range(len(tuple_status)):
            print(f"[{i}]: {tuple_status[i]}")
        input_status = input()
        if input_status != "":
            # Проверяем ввод. Если есть цифра или слово из списка - меняем
            if input_status.capitalize() in tuple_status:
                return input_status
            if input_status.isdigit() and int(input_status) in range(len(tuple_status)):
                return tuple_status[int(input_status)]
            else:
                print(Fore.LIGHTRED_EX + "\nНет такого статуса в списке. Введите статус заново.")

# Ввод элемента и его проверка на пустую строку.
def get_input(text):
    value = input(Fore.LIGHTYELLOW_EX + text).capitalize()
    while value == "":
        print(Fore.LIGHTRED_EX + "Пустой ввод! Введите значение.")
        value = input(Fore.LIGHTYELLOW_EX + text).capitalize()
    return value

# Создание одной заметки
def create_one_note(notes):
    note = {
        tuple_keys[0] : generate_unique_id(notes),
        tuple_keys[1] : get_input(Back.RESET + "Введите имя пользователя: "),
        tuple_keys[2] : get_input("Введите заголовок заметки: "),
        tuple_keys[3] : get_input("Введите описание заметки: "),
        tuple_keys[4] : get_status(),
        tuple_keys[5] : str(get_date("начала")),
        tuple_keys[6] : str(get_date("конца"))
    }
    return note

def generate_unique_id(notes):
    # Решил использовать числа меньше, методом Рандома (до 10000 значений).
    # Если потом понадобится масштабировать - возьму uuid.
    while True:
        id = random.randint(1, 10_000)
        # Проверка уникального значения.
        for i in range(len(notes)):
            if id == notes[i][tuple_keys[0]]:
                break
        else:
            return id
    # По умолчанию в задании.
    #return uuid.uuid4()

# Добавление заметки в словарь.
def add_note (notes):
    check_new_note = True
    while check_new_note:
        notes.append(create_one_note(notes))
        if input(Fore.LIGHTCYAN_EX + "Если Вы хотите добавить еще одну заметку введите 'Да':").capitalize() != "Да":
            check_new_note = False