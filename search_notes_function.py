from colorama import Fore, Style

notes = [
    {'ID': "1", 'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю', 'Статус': 'новая', 'Дата начала': '27-11-2024', 'Дата истечения': '30-11-2024'},
    {'ID': "2", 'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'в процессе', 'Дата начала': '25-11-2024', 'Дата истечения': '01-12-2024'},
    {'ID': "3", 'Имя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект', 'Статус': 'выполнено', 'Дата начала': '20-11-2024', 'Дата истечения': '26-11-2024'}
]
tuple_keys = ("ID", "Имя", "Заголовок", "Описание", "Статус", "Дата начала", "Дата истечения")

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
                if i % 5 == 0 and i != 0 and j == 0:
                    input(Fore.LIGHTCYAN_EX + "Для продолжения ввода нажмите Enter:")
                print(Fore.MAGENTA + f'{str(note[i][tuple_keys[j]]):{max_columns[j] + 1}}', end='|')
            print()

# Мини функция возвращает bool, если найдено совпадение.
def search_logic (notes, i, j, keyword=None, status=None):
    return ((keyword is not None and status is not None and keyword.lower() in notes[i][tuple_keys[j]].lower() and status.lower() == notes[i][tuple_keys[4]].lower())
            or (status is not None and status.lower() == notes[i][tuple_keys[4]].lower())
            or (keyword is not None and keyword.lower() in notes[i][tuple_keys[j]].lower()))

#Непосредственно функция поиска.
def search_notes(notes, keyword=None, status=None):
    note = []
    if keyword is None and status is None:
        print(Fore.LIGHTRED_EX + "Ключевых слов не указано! Поиск не был произведен.")
        return
    for i in range(len(notes)):
        for j in range(1, len(tuple_keys)):
            if search_logic(notes, i, j, keyword, status):
                note.append(notes[i])
                break
    if note:
        display_note(note)
    else:
        print(Fore.LIGHTRED_EX + "Совпадений не найдено!")

search_notes(notes)
search_notes(notes, keyword='покупок')
search_notes(notes, status='в процессе')
search_notes(notes, keyword='работы', status='выполнено')