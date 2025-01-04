from datetime import datetime, timedelta

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
        print("Дата задачи введена некорректно! Повторите ввод.")
        return 1
    return formated_date

# Сравнение даты + возврат даты.
def get_date (word, date = None, issue_date = datetime.strptime("3000-01-01", "%Y-%m-%d").date()):
    date_today = datetime.today().date()
    print(f"Введите дату {word} задачи через дефис, например 31-12-2024:")
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
            print("Дата начала заметки установлена на сегодня.")
            return date_today
        else:
            print("Дата истечения заметки установлена через 7 дней.")
            return date_today + timedelta(7)

    # Если не пустая строка, то
    formated_date = create_date(str_date)
    while formated_date == 1:
        formated_date = create_date(input(f"Введите дату {word} задачи через дефис, например 31-12-2024:"))

    # Дата начала меньше даты истечения. (Проверка)
    if word.capitalize() == "Начала":
        if formated_date > issue_date:
            print("Введенная дата начала больше, чем дата истечения. Изменения не внесены.")
            return date

    # Дата конца больше текущей даты. (Проверка)
    if word.capitalize() == "Конца":
        if formated_date < date_today:
            if date is None:
                print(f"Дата {word} задачи сегодня!")
                return date_today
            else:
                print("Введенная дата истечения меньше, чем текущая. Изменения не внесены.")
                return date

    temp_days = int((date_today - formated_date).days)
    if  temp_days > 0:
        print(f"Дата {word} задачи началась {temp_days} дня назад.")
    elif temp_days == 0:
        print(f"Дата {word} задачи сегодня!")
    elif temp_days < 0:
        print(f"Дата {word} задачи через {(temp_days)} дня.")
    return formated_date

#Ввод статуса заявки из списка, остальные статусы отбрасываются.
def get_status():
    status = ""
    check_status = True
    tuple_status = ("Новая", "В процессе", "Отложено", "Выполнено", "Отменено")
    while check_status:
        print("\nВведите статус из списка ниже. Вы можете ввести его полностью или указать число.")
        print("Список статусов:")
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
                print("\nНет такого статуса в списке. Статус не изменен.")

# Ввод элемента и его проверка на пустую строку.
def get_input(text):
    value = input(text).capitalize()
    while value == "":
        print("Пустой ввод! Введите значение.")
        value = input(text).capitalize()
    return value

# Создание одной заметки
def create_one_note():
    note = {
        "Имя": get_input("Введите имя пользователя: "),
        "Описание": get_input("Введите описание заметки: "),
        "Заголовок": get_input("Введите заголовок заметки: "),
        "Статус": get_status(),
        "Дата создания заметки": get_date("начала"),
        "Дата истечения активности заметки": get_date("конца")
    }
    return note

# Добавление заметки в словарь.
def add_note (notes):
    check_new_note = True
    while check_new_note:
        count = 1
        if notes:
            nk = notes.keys()
            check_exist = True

            for i in range(len(nk)):
                count += i
                if count not in nk:
                    check_exist = False
                    break
            if check_exist:
                count = len(nk) + 1

        notes[count] = create_one_note()
        if input("Если Вы хотите добавить еще одну заметку введите 'Да':").capitalize() != "Да":
            check_new_note = False

# Обновление значения.
def update_note(notes):
    tuple_keys = ("Имя", "Описание", "Заголовок", "Статус", "Дата создания заметки", "Дата истечения активности заметки")
    num = int(input("Введите номер заявки, который хотите обновить:"))

    # Проверка номера заявки.
    if num in notes.keys():
        check_key = True
        while check_key:
            print("Список ключей:")
            for i in range(len(tuple_keys)):
                print(f"[{i}]: {tuple_keys[i]}")
            key = int(input("Введи номер ключа для изменения из списка:"))
            # Проверка ключа. Если есть совпадение - вызываем соответствующую функцию.
            if key in range(len(tuple_keys)):
                temp = ""
                if key == 0:
                    temp = get_input("Введите новое имя пользователя: ")
                if key == 1:
                    temp = get_input("Введите новое описание заметки: ")
                if key == 2:
                    temp = get_input("Введите новый заголовок заметки: ")
                if key == 3:
                    temp = get_status()
                if key == 4:
                    temp = get_date("начала", notes[num][tuple_keys[4]], notes[num][tuple_keys[5]])
                if key == 5:
                    temp = get_date("конца", notes[num][tuple_keys[5]])
                if input("Если Вы уверены, что хотите обновить поле введите Да:").capitalize() == "Да":
                    notes[num][tuple_keys[key]] = temp
                    print(f"В заметке №{num} ключ {tuple_keys[key]} изменен на {notes[num][tuple_keys[key]]}")
                else:
                    print("Пользователь отказался от внесения изменений.")
            else:
                print("Нет ключа c таким номером.")
            if input("Вы хотите внести другие изменения в эту заметку? ").capitalize() != "Да":
                display_note(notes[num])
                check_key = False

#Удаление заявки (проверка и вызов удаления)
def delete_note(notes):
    # Подфункция фактического удаление заметки
    def sub_del(text, key, note):
        check_user = True
        for k, n in note.items():
            if text == n[key]:
                print("Следующая заявка будет удалена:")
                display_note(notes[k])
                notes.pop(k)
                check_user = False
        if check_user:
            print("У данного пользователя нет заметок. Заметки не удалены!")

    if notes:
        note_list = notes.copy()
        print("Выберите, что удаляем:")
        print("[0]: Все заметки пользователя.")
        print("[1]: Заметку с определенным заголовком. (для всех пользователей)")
        input_choice = input()
        if int(input_choice) == 0: # Удаление по имени пользователя всех его заметок
            user = input("Введите имя пользователя: ")
            sub_del(user, "Имя", note_list)
        elif int(input_choice) == 1:
            title = input("Введите заголовок: ")
            sub_del(title, "Заголовок", note_list)
        else:
            print("Некорректный ввод. Заметки не удалены!")
    else:
        print("Нет сохраненных заметок!")

# Форматированный вывод списка
def display_note (note):
    for key, value in note.items():
        print(f"{key.capitalize()}: {value}")

tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку", "Выход")
notes = {} #Файл для хранения всех заметок.
check_menu = True
print("Добро пожаловать в Менеджер заметок!")
while check_menu:
    print("\nГлавное меню.")
    print("Выберите пункт из меню, вводом нужной цифры:")
    for i in range(len(tuple_menu)):
        print(f"[{i}]: {tuple_menu[i]}")
    input_menu = int(input())
    if input_menu == 0:
        if notes:
            print("\nСобранная информация о заметках:")
            for id, note in notes.items():
                print(f"\n[{id} заметка:")
            display_note(note)
        else:
            print("Нет сохраненных заметок.")
    elif input_menu == 1:
        add_note(notes)
    elif input_menu == 2:
        delete_note(notes)
    elif input_menu == 3:
        if notes:
            print("\nСобранная информация о заметках:")
            for id, note in notes.items():
                print(f"\n[{id} заметка:")
                display_note(note)
                update_note(notes)
        else:
            print("Нет сохраненных заметок.")
    elif input_menu == 4:
        print("Программа завершается, до свидания!")
        exit(0)