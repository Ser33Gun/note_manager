from datetime import datetime

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
def get_date (word):
    date_today = datetime.today().date()
    str_date = input("Введите дату " + word + " задачи через дефис, например 31-12-2024:")
    formated_date = create_date(str_date)
    while formated_date == 1:
        formated_date = create_date(input("Введите дату" + word + "задачи через дефис, например 31-12-2024:"))
    temp_days = int((date_today - formated_date).days)
    if  temp_days > 0:
        print("Дата " + word + " задачи началась " + str(temp_days) + "дня назад.")
    elif temp_days == 0:
        print("Дата " + word + " задачи сегодня!")
    elif temp_days < 0:
        print("Дата " + word + " задачи через " + str(abs(temp_days)) + " дня.")
    return formated_date

# Сборка пунктов заметки, проверка на дубли.
def get_titles():
    check_next_title = True  # Чек пустой строки
    list = []
    while check_next_title:
        title = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
        if title != "":
            check_title = True  # Чек совпадения
            for tle in list:
                if title == tle:
                    check_title = False  # Если совпало - переключаем чек
            if check_title:
                list.append(title)
        else:
            check_next_title = False
    return list

#Ввод заявки из списка, остальные отбрасываются.
def get_status():
    status = ""
    check_status = True
    tuple_status = ("Новая", "В процессе", "Отложено", "Выполнено", "Отменено")
    while check_status:
        print("\nВведите статус из списка ниже. Вы можете ввести его полностью или указать число.")
        print("\nСписок статусов:")
        for i in range(len(tuple_status)):
            print("[" + str(i) + "]: " + tuple_status[i])
        input_status = input()
        check_input = True
        if input_status != "":
            # Проверяем ввод. Если есть цифра или слово из списка - меняем
            for i in range(len(tuple_status)):
                if input_status.capitalize() == tuple_status[i] or (input_status.isdigit() and int(input_status) == i):
                    return tuple_status[i]
            if check_input:
                print("\nНет такого статуса в списке. Статус не изменен.")

# Создание одной заметки
def create_one_note():
    note = {
        "username": input("Введите имя пользователя: "),
        "content": input("Введите описание заметки: "),
        "titles": get_titles(),
        "status": get_status(),
        "created_date": get_date("начала"),
        "issue_date": get_date("конца")
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
        print("Если Вы хотите добавить еще одну заметку введите 'Да':")
        if input().capitalize() != "Да":
            check_new_note = False

# Форматированный вывод заметки
def print_note (note):
    for key, value in note.items():
        if key == "titles":
            for tle in note.get("titles"):
                print(f"{key.capitalize()}: {tle}")
            continue
        print(f"{key.capitalize()}: {value}")

notes = {} #Файл для хранения всех заметок.
add_note(notes)

print("\nСобранная информация о заметках:")
for id, note in notes.items():
    print(id.__str__() + " заметка:")
    print_note(note)