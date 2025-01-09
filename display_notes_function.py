from colorama import Fore, Back, Style
from create_note_function import tuple_keys


# Форматированный вывод списка
def display_note (note, key = None, full = True):
    max_columns = []
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
                if i % 5 == 0 and i :
                    input(Fore.LIGHTCYAN_EX + "Для продолжения ввода нажмите Enter:")
                print(Fore.MAGENTA + f'{str(note[i][tuple_keys[j]]):{max_columns[j] + 1}}', end='|')
            print()