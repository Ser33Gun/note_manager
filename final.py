# Базовый вариант через создание списка.
#
# Запрашиваем у пользователя информацию для создания заметки
#username = input("Введите имя пользователя: ")
#titles = []
#for i in range(3):
#    title = input(f"Введите заголовок заметки {i + 1}: ")
#    titles.append(title)
#
#content = input("Введите описание заметки: ")
#status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
#created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
#issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")
#note = [
#    username,
#    titles,
#    content,
#    status,
#    created_date,
#    issue_date
#]
#print(note)

# Модифицированный вариант через создание словаря.
# Создание и инициализация словаря.
note = {
    "username": input("Введите имя пользователя: "),
    "titles": [],
    "content": input("Введите описание заметки: "),
    "status": input("Введите статус заметки (например, 'Активна', 'Выполнена'): "),
    "created_date" : input("Введите дату создания заметки в формате 'день-месяц-год': "),
    "issue_date" : input("Введите дату истечения заметки в формате 'день-месяц-год': ")
}

# Добавляем заголовки в список внутри словаря
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    note["titles"].append(title)

# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    if key == "created_date" or key == "issue_date":
        print(f"{key.capitalize()}: {value[:5]}")
    else:
        print(f"{key.capitalize()}: {value}")
