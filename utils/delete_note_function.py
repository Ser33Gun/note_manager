from colorama import Fore
from interface import display_note
from utils import tuple_keys

def delete_note(notes):
    # Подфункция фактического удаление заметки
    def sub_del(text, key):
        check_note = True
        for i in reversed(range(len(notes))):
            if str(text) in notes[i][key]:
                print(Fore.LIGHTGREEN_EX +"Следующая заявка будет удалена:")
                display_note(notes, i)
                if input(Fore.LIGHTCYAN_EX + "\nЕсли Вы хотите удалить данную заявку введите Да:").capitalize() == "Да":
                    notes.pop(i)
                    print(Fore.LIGHTGREEN_EX + "Заметка успешно удалена!")
                check_note = False
        if check_note:
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