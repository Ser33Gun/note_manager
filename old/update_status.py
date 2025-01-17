# Создание и инициализация словаря.

tuple_status = ("В процессе", "Отложено", "Выполнено", "Отменено")

note = {
    "username": input("Введите имя пользователя: "),
    "titles": [],
    "content": input("Введите описание заметки: "),
    "status": input("Введите статус заметки (например, 'В процессе', 'Выполнена'): "),
    "created_date" : input("Введите дату создания заметки в формате 'день-месяц-год': "),
    "issue_date" : input("Введите дату истечения заметки в формате 'день-месяц-год': ")
}
#Цикл для ввода заголовков
check_next_title = True #Чек пустой строки
while check_next_title:
    title = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
    print(note.get("titles"))
    if title != "":
        if title not in note.get("titles"):
            note["titles"].append(title)
    else:
        check_next_title = False

#Предложение поменять статус на один из списка. В случае несовпадения - статус не меняется.
print("\nТекущий статус заметки: " + note.get("status"))
print("\nЕсли Вы хотите поменять статус, то введите новый статус из списка ниже. Если нет - введите пустую строку.")
print("\nСписок статусов:")
for i in range(len(tuple_status)):
    print("[" + str(i) + "]: " + tuple_status[i])

check_status = True
while check_status:
    input_status = input("Введите цифру или название статуса:")
    if input_status != "":
        # Проверяем ввод. Если есть цифра или слово из списка - меняем
        for i in range(len(tuple_status)):
            if input_status.capitalize() == tuple_status[i] or (input_status.isdigit() and int(input_status)== i):
                note["status"] = tuple_status[i]
            check_status = False
            print("\nСтатус изменен на " + tuple_status[i] + ".")
        if check_status:
            print("\nНет такого статуса в списке. Статус не изменен.")

#Вывод всей заметки в структурированном виде.
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