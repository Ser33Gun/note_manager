from colorama import Fore, Style
from utils import tuple_keys

# Сортировка списка для вывода
def sort_for_display(note):
    if input(Fore.LIGHTCYAN_EX +"Если Вы хотите отсортировать вывод списка, то введите Да:").capitalize() == "Да":
        print(Fore.LIGHTWHITE_EX + "Список ключей для сортировки:")
        for j in range(len(tuple_keys)):
            print(f"[{j}]: {tuple_keys[j]}")
        key = int(input(Fore.LIGHTYELLOW_EX + "Введите номер ключа для изменения из списка:"))
        while not key in range(len(tuple_keys)):
            key = int(input(Fore.LIGHTRED_EX + "Неверно введен ключ. Введите номер ключа для изменения из списка:"))
        if input(Fore.LIGHTCYAN_EX +"Если Вы хотите отсортировать список в обратном порядке, то введите Да:").capitalize() == "Да":
            s = True
        else:
            s = False
        # Лямбда-функцию честно слямзил с интернета, сам не особо понимаю, что она делает.
        return sorted(note, key = lambda x: x[tuple_keys[key]], reverse=s)
    else:
        return note

# Форматированный вывод списка
def display_note (note, key = None, full = True):
    if not note:
        print(Fore.LIGHTRED_EX + "Нет сохраненных заметок.")
        return
    note = sort_for_display(note)
    if input(Fore.LIGHTCYAN_EX + "\nЕсли Вы хотите получить только ID, имя пользователя и заголовок заметки, введите Да:").capitalize() == "Да":
        full = False
    print(Fore.LIGHTGREEN_EX + "Собранная информация о заметках:")
    max_columns = [] # Максимальная длина столбца для вывода.
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
                if i % 5 == 0 and i and not j:
                    input(Fore.LIGHTCYAN_EX + "Для продолжения ввода нажмите Enter:")
                print(Fore.MAGENTA + f'{str(note[i][tuple_keys[j]]):{max_columns[j] + 1}}', end='|')
            print()