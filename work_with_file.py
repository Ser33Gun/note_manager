from colorama import Fore
from json import JSONDecodeError
from create_note_function import tuple_keys
import json

def save_notes_to_file(notes, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(len(notes)):
            for j in range(len(tuple_keys)):
                file.writelines(f"{tuple_keys[j]}:{notes[i][tuple_keys[j]]}\n")

def load_notes_from_file(file_name):
    notes = []
    temp_tuple = {}
    try:
        file = open(file_name, 'r', encoding='utf-8')
    except FileNotFoundError:
       print(Fore.LIGHTRED_EX + f"Файл {file_name} не найден." + Fore.LIGHTCYAN_EX + " Создан пустой файл.")
       with open(file_name, 'x', encoding='utf-8') as file:
           return []
    except UnicodeDecodeError:
        print(Fore.LIGHTRED_EX + "Не удалось декодировать файл! Функция остановлена!")
        return []
    except PermissionError:
        print(Fore.LIGHTRED_EX + "Нет доступа к файлу! Функция остановлена!")
        return []
    except:
        print(Fore.LIGHTRED_EX + "Неизвестная ошибка. Функция остановлена!")
        return []

    text = file.read().split('\n')
    count = 0
    for s in text:
        if s:
            split = s.split(':')
            if split[0].capitalize() in tuple_keys:
                temp_tuple[split[0]] = split[1]
                count += 1
            if count % len(tuple_keys) == 0 and count:
                # Вставляем словарь в список и обнуляем словарь.
                notes.append(temp_tuple)
                count = 0
                temp_tuple = {}
    file.close()
    return notes

def append_notes_to_file(notes, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for i in range(len(notes)):
            for j in range(len(tuple_keys)):
                file.writelines(f"{tuple_keys[j]}:{notes[i][tuple_keys[j]]}\n")

def save_notes_json(notes, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        data = json.dumps(notes, indent=4, ensure_ascii=False)
        file.write(data)
    print(Fore.LIGHTGREEN_EX + "Запись в файл произведена успешно!")

def load_notes_json(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            try:
                json_dict = json.loads(file.read())
            except JSONDecodeError:
                print(Fore.LIGHTRED_EX + f"Файл {file_name} пуст или поврежден.")
                return []
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + f"Файл {file_name} не найден." + Fore.LIGHTCYAN_EX + " Создан пустой файл. Запустите функцию заново.")
        with open(file_name, 'x', encoding='utf-8') as file:
            return []
    print(Fore.LIGHTGREEN_EX + "Чтение из файла произведена успешно!")
    return json_dict