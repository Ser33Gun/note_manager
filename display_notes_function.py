from datetime import datetime, timedelta
from colorama import Fore, Back, Style

tuple_keys = ("ID", "Имя", "Заголовок", "Описание", "Статус", "Дата начала", "Дата истечения")

# Перевод строки в дату, если строка дана в одном из 6 форматов.
def create_date (str_date):
    formated_date = ""
    date_formats = ("%Y-%m-%d", "%Y-%d-%m", "%m-%d-%Y", "%m-%Y-%d", "%d-%m-%Y", "%d-%m-%Y")
    for i in date_formats:
        try:
            formated_date = datetime.strptime(str_date, i).date()
        except ValueError:
            pass
    if formated_date == "":
        print(Fore.LIGHTRED_EX + "Дата задачи введена некорректно! Повторите ввод.")
        return 1
    return formated_date

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
    while formated_date == 1:
        formated_date = create_date(input(Fore.LIGHTYELLOW_EX + f"Введите дату {word} задачи через дефис, например 31-12-2024:"))

    # Дата начала меньше даты истечения. (Проверка)
    if word.capitalize() == "Начала":
        if formated_date > issue_date:
            print(Fore.LIGHTRED_EX + "Введенная дата начала больше, чем дата истечения. Изменения не внесены.")
            return date

    # Дата конца больше текущей даты. (Проверка)
    if word.capitalize() == "Конца":
        if formated_date < date_today:
            if date is None:
                print(Fore.LIGHTGREEN_EX + f"Дата {word} задачи сегодня!")
                return date_today
            else:
                print(Fore.LIGHTRED_EX + "Введенная дата истечения меньше, чем текущая. Изменения не внесены.")
                return date

    temp_days = int((date_today - formated_date).days)
    if  temp_days > 0:
        print(Fore.LIGHTGREEN_EX + f"Дата {word} задачи началась {temp_days} дня назад.")
    elif temp_days == 0:
        print(Fore.LIGHTGREEN_EX + f"Дата {word} задачи сегодня!")
    elif temp_days < 0:
        print(Fore.LIGHTGREEN_EX + f"Дата {word} задачи через {(temp_days)} дня.")
    return formated_date

#Ввод статуса заявки из списка, остальные статусы отбрасываются.
def get_status():
    check_status = True
    tuple_status = ("Новая", "В процессе", "Отложено", "Выполнено", "Отменено")
    while check_status:
        print(Fore.LIGHTYELLOW_EX + "\nВведите статус из списка ниже. Вы можете ввести его полностью или указать число.")
        print(Fore.LIGHTWHITE_EX + "Список статусов:")
        for i in range(len(tuple_status)):
            print(f"[{i}]: {tuple_status[i]}")
        input_status = input()
        check_input = True
        if input_status != "":
            # Проверяем ввод. Если есть цифра или слово из списка - меняем
            for i in range(len(tuple_status)):
                if input_status.capitalize() == tuple_status[i] or (input_status.isdigit() and int(input_status) == i):
                    return tuple_status[i]
            if check_input:
                print(Fore.LIGHTRED_EX + "\nНет такого статуса в списке. Статус не изменен.")

# Ввод элемента и его проверка на пустую строку.
def get_input(text):
    value = input(Fore.LIGHTYELLOW_EX + text).capitalize()
    while value == "":
        print(Fore.LIGHTRED_EX + "Пустой ввод! Введите значение.")
        value = input(Fore.LIGHTYELLOW_EX + text).capitalize()
    return value

# Создание одной заметки
def create_one_note(id):
    note = {
        tuple_keys[0] : str(id),
        tuple_keys[1] : get_input(Back.RESET + "Введите имя пользователя: "),
        tuple_keys[2]: get_input("Введите заголовок заметки: "),
        tuple_keys[3] : get_input("Введите описание заметки: "),
        tuple_keys[4] : get_status(),
        tuple_keys[5] : get_date("начала"),
        tuple_keys[6] : get_date("конца")
    }
    return note

# Добавление заметки в словарь.
def add_note (notes):
    check_new_note = True
    while check_new_note:
        count = 1
        check_exist = True

        #Подбор первого свободного значения ID.
        while check_exist:
            if len(notes) > 0:
                for i in range(len(notes)):
                    if str(count) == notes[i][tuple_keys[0]]:
                        check_exist = True
                        count += 1
                        break
                    else:
                        check_exist = False
            else:
                check_exist = False
        notes.append(create_one_note(count))
        if input(Fore.LIGHTCYAN_EX + "Если Вы хотите добавить еще одну заметку введите 'Да':").capitalize() != "Да":
            check_new_note = False

# Обновление значения.
def update_note(notes):
    id = str(input(Fore.LIGHTYELLOW_EX + "Введите номер заявки, который хотите обновить:"))

    # Проверка номера заявки.
    for i in range(len(notes)):
        if id in notes[i][tuple_keys[0]]:
            check_key = True
            while check_key:
                print(Fore.LIGHTWHITE_EX + "Список ключей для изменения.:")
                for j in range(1, len(tuple_keys)):
                    print(f"[{j}]: {tuple_keys[j]}")
                key = int(input(Fore.LIGHTYELLOW_EX + "Введи номер ключа для изменения из списка:"))

                # Проверка ключа. Если есть совпадение - вызываем соответствующую функцию.
                # ID - внутреннее значение, не даем изменить.
                if key in range(len(tuple_keys)):
                    temp = ""
                    if key == 1:
                        temp = get_input("Введите новое имя пользователя: ")
                    elif key == 2:
                        temp = get_input("Введите новый заголовок заметки: ")
                    elif key == 3:
                        temp = get_input("Введите новое описание заметки: ")
                    elif key == 4:
                        temp = get_status()
                    elif key == 5:
                        temp = get_date("начала", notes[i][tuple_keys[4]], notes[i][tuple_keys[5]])
                    elif key == 6:
                        temp = get_date("конца", notes[i][tuple_keys[5]])

                    # Уточняем перед внесением изменений.
                    if input(Fore.LIGHTCYAN_EX + "Если Вы уверены, что хотите обновить поле, введите Да:").capitalize() == "Да":
                        notes[i][tuple_keys[key]] = temp
                        print(Fore.LIGHTGREEN_EX + f"В заметке №{i} ключ {tuple_keys[key]} изменен на {notes[i][tuple_keys[key]]}")
                    else:
                        print(Fore.LIGHTCYAN_EX + "Пользователь отказался от внесения изменений.")
                else:
                    print(Fore.LIGHTRED_EX + "Нет ключа c таким номером.")
                if input(Fore.LIGHTCYAN_EX + "Вы хотите внести другие изменения в эту заметку? ").capitalize() != "Да":
                    display_note(notes, i)
                    check_key = False

#Удаление заявки (проверка и вызов удаления)
def delete_note(notes):
    # Подфункция фактического удаление заметки
    def sub_del(text, key):
        check_user = True
        #temp_notes = notes.copy()
        for i in reversed(range(len(notes))):
            if str(text) == notes[i][key]:
                print(Fore.LIGHTGREEN_EX +"Следующая заявка будет удалена:")
                display_note(notes, i)
                notes.pop(i)
                check_user = False
        if check_user:
            print(Fore.LIGHTRED_EX +"Нет подходящих заметок для удаления.")

    if notes:
        print(Fore.RED + "Выберите, что удаляем:")
        print(Fore.LIGHTWHITE_EX + "[0]: Заметку с выбранным ID.")
        print("[1]: Все заметки пользователя.")
        print("[2]: Заметку с определенным заголовком. (для всех пользователей)")
        input_choice = int(input())
        if input_choice == 0: # Удаление заметки по ID
            id = input(Fore.LIGHTYELLOW_EX + "Введите номер ID: ")
            sub_del(id, tuple_keys[input_choice])
        elif int(input_choice) == 1: # Удаление по имени пользователя всех его заметок
            user = input(Fore.LIGHTYELLOW_EX + "Введите имя пользователя: ")
            sub_del(user, tuple_keys[input_choice])
        elif int(input_choice) == 2:
            title = input(Fore.LIGHTYELLOW_EX + "Введите заголовок: ")
            sub_del(title, tuple_keys[input_choice])
        else:
            print(Fore.RED + "Некорректный ввод. Заметки не удалены!")
    else:
        print(Fore.LIGHTRED_EX + "Нет сохраненных заметок!")

# Форматированный вывод списка
def display_note (note, key = None, full = True):
    max_columns = []
    print(len(note))
    # Получаем максимальную длину столбца.
    for j in range(len(tuple_keys)):
        len_el = []
        for i in range(len(note)):
            if len(str(note[i][tuple_keys[j]])) >= len(tuple_keys[j]):
                len_el.append(len(note[i][tuple_keys[j]]))
            else:
                len_el.append(len(tuple_keys[j]))
        max_columns.append(max(len_el))

    # Таблично выводим значения + красим вывод.
    if full:
        end = len(tuple_keys)
        eq = sum(max_columns) + 14
    else:
        end = 3
        eq = sum(max_columns[:3]) + 6
    for i in range(end):
        print(Fore.LIGHTBLUE_EX + Style.NORMAL + f'{tuple_keys[i]:{max_columns[i] + 1}}', end='|')
    print()
    print(Fore.LIGHTWHITE_EX + f'{"=" * eq}')
    for i in range(len(note)):
        if key is not None:
            if i == key:
                for j in range(end):
                    print(Fore.MAGENTA + f'{str(note[i][tuple_keys[j]]):{max_columns[j] + 1}}', end='|')
        else:
            for j in range(end):
                if i % 5 == 0 and i != 0 and j == 0:
                    input(Fore.LIGHTCYAN_EX + "Для продолжения ввода нажмите Enter:")
                print(Fore.MAGENTA + f'{str(note[i][tuple_keys[j]]):{max_columns[j] + 1}}', end='|')
            print()


# Меню.
tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку", "Выход")
notes = [{'ID': '1', 'Имя': 'Сергей', 'Заголовок': 'З', 'Описание': 'О', 'Статус': 'Новая', 'Дата начала': str(datetime.strptime("2025-01-08", "%Y-%m-%d")), 'Дата истечения': str(datetime.strptime("2025-01-15", "%Y-%m-%d"))},
         {'ID': '2', 'Имя': 'Сергей', 'Заголовок': 'За', 'Описание': 'Оп', 'Статус': 'Новая', 'Дата начала': str(datetime.strptime("2025-01-08", "%Y-%m-%d")), 'Дата истечения': str(datetime.strptime("2025-01-15", "%Y-%m-%d"))},
         {'ID': '3', 'Имя': 'Сергей', 'Заголовок': 'Заг', 'Описание': 'Опи', 'Статус': 'Новая', 'Дата начала': str(datetime.strptime("2025-01-08", "%Y-%m-%d")), 'Дата истечения': str(datetime.strptime("2025-01-15", "%Y-%m-%d"))}] # Файл для хранения всех заметок.
check_menu = True
print(Fore.LIGHTWHITE_EX + "Добро пожаловать в Менеджер заметок!")
while check_menu:
    print("\n" + Back.RESET + Fore.LIGHTWHITE_EX + "Главное меню.")
    print("Выберите пункт из меню, вводом нужной цифры:")
    for i in range(len(tuple_menu)):
        print(f"[{i}]: {tuple_menu[i]}")
    input_menu = int(input())
    if input_menu == 0:
        if notes:
            full = True
            if input(
                    Fore.LIGHTCYAN_EX + "\n Если Вы хотите получить только имя пользователя и заголовок заметки, введите Да:").capitalize() == "Да":
                full = False
            print(Fore.GREEN + "Собранная информация о заметках:")
            display_note(notes,None ,full)
        else:
            print(Fore.RED + "Нет сохраненных заметок.")
    elif input_menu == 1:
        add_note(notes)
    elif input_menu == 2:
        delete_note(notes)
    elif input_menu == 3:
        if notes:
            print("\n" + Fore.RED + "Собранная информация о заметках:")
            display_note(notes)
            update_note(notes)
        else:
            print(Fore.RED + "Нет сохраненных заметок.")
    elif input_menu == 4:
        print(Fore.LIGHTGREEN_EX +"Программа завершается, до свидания!")
        exit(0)