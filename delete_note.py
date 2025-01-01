from datetime import datetime

from update_status import check_title


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
def add_titles():
    check_next_title = True  # Чек пустой строки
    title_list = []
    while check_next_title:
        title = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
        if title != "":
            check_title = True  # Чек совпадения
            for tle in title_list:
                if title == tle:
                    check_title = False  # Если совпало - переключаем чек
            if check_title:
                title_list.append(title.capitalize())
        else:
            check_next_title = False
    return title_list

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
        "Имя": input("Введите имя пользователя: ").capitalize(),
        "Описание": input("Введите описание заметки: ").capitalize(),
        "Заголовок": add_titles(),
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
        print("Если Вы хотите добавить еще одну заметку введите 'Да':")
        if input().capitalize() != "Да":
            check_new_note = False

def delete_note(notes):
    if notes:
        note_list = notes.copy()
        print("Выберите, что удаляем:")
        print("[0]: Все заметки пользователя.")
        print("[1]: Заметку с определенным заголовком. (для всех пользователей)")
        input_choice = input()
        if int(input_choice) == 0: # Удаление по имени пользователя всех его заметок
            user = input("Введите имя пользователя: ")
            check_user = True
            for key, n in note_list.items():
                if user == n["Имя"]:
                    print("Следующая заявка будет удалена:") # В целом можно вынести в отдельную функцию,
                    print_note(notes[key])                   # если будут еще варианты удаления.
                    notes.pop(key)
                    check_user = False
                if check_user:
                    print("У данного пользователя нет заметок. Заметки не удалены!")
        elif int(input_choice) == 1:
            title = input("Введите заголовок: ")
            check_t = True
            for key, n in note_list.items():
                for t in n["Заголовок"]:
                    print(t)
                    if title == t:
                        print("Следующая заявка будет удалена:")
                        print_note(notes[key])
                        notes.pop(key)
                        check_t = False
            if check_t:
                print("Заметки с таким заголовком не найдены. Заметки не удалены!")
        else:
            print("Некорректный ввод. Заметки не удалены!")
    else:
        print("Нет сохраненных заметок!")

# Форматированный вывод списка
def print_note (note):
    for key, value in note.items():
        if key == "titles":
            for tle in note.get("titles"):
                print(f"{key.capitalize()}: {tle}")
            continue
        print(f"{key.capitalize()}: {value}")

tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку(NIY)", "Выход")
notes = {} #Файл для хранения всех заметок.
check_menu = True
print("Добро пожаловать в Менеджер заметок!")
while check_menu:
    print("\nГлавное меню.")
    print("Выберите пункт из меню, вводом нужной цифры:")
    for i in range(len(tuple_menu)):
        print("[" + str(i) + "]: " + tuple_menu[i])
    input_menu = int(input())
    if input_menu == 0:
        print("\nСобранная информация о заметках:")
        for id, note in notes.items():
            print(id.__str__() + " заметка:")
            print_note(note)
    elif input_menu == 1:
        add_note(notes)
    elif input_menu == 2:
        delete_note(notes)
    elif input_menu == 3:
        print("На данный момент функция не реализована, ожидайте.")
    elif input_menu == 4:
        print("Программа завершается, до свидания!")
        exit(0)
