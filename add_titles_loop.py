# Создание и инициализация словаря.
note = {
    "username": input("Введите имя пользователя: "),
    "titles": [],
    "content": input("Введите описание заметки: "),
    "status": input("Введите статус заметки (например, 'Активна', 'Выполнена'): "),
    "created_date" : input("Введите дату создания заметки в формате 'день-месяц-год': "),
    "issue_date" : input("Введите дату истечения заметки в формате 'день-месяц-год': ")
}
#Цикл для ввода заголовков
check_next_title = True #Чек пустой строки
while check_next_title:
    title = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
    if title != "":
        check_title = True # Чек совпадения
        for tle in note.get("titles"):
            if title == tle:
                check_title = False # Если совпало - переключаем чек
        if check_title:
            note["titles"].append(title)
    else:
        check_next_title = False

print("\nСобранная информация о заметке:")
for key, value in note.items():
    if key == "titles":
        for tle in note.get("titles"):
            print(f"{key.capitalize()}: {tle}")
        continue
    if key == "created_date" or key == "issue_date":
        print(f"{key.capitalize()}: {value[:5]}")
    else:
        print(f"{key.capitalize()}: {value}")