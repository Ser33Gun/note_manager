from colorama import Fore
import create_note_function as cnf
from create_note_function import tuple_keys
from display_notes_function import display_note

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
                        temp = cnf.get_input("Введите новое имя пользователя: ")
                    elif key == 2:
                        temp = cnf.get_input("Введите новый заголовок заметки: ")
                    elif key == 3:
                        temp = cnf.get_input("Введите новое описание заметки: ")
                    elif key == 4:
                        temp = cnf.get_status()
                    elif key == 5:
                        temp = cnf.get_date("начала", notes[i][tuple_keys[4]], notes[i][tuple_keys[5]])
                    elif key == 6:
                        temp = cnf.get_date("конца", notes[i][tuple_keys[5]])

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