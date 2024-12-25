#from datetime import datetime

# Запрашиваем информацию у пользователя
username = input("Введите имя пользователя: ") # Имя пользователя
title = input("Введите заголовок заметки: ") # Заголовок заметки
content = input("Введите описание заметки: ") # Описание заметки
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ") # Статус заметки
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ") # Дата создания заметки
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ") # Дата истечения заметки

#Обрезание через извлечение подстроки
temp_created_date = created_date[:5]
temp_issue_date = issue_date[:5]

# Обрезание через создание типа datetime
#date_format = "%d-%m-%Y"
#temp_created_date = datetime.strptime(created_date, date_format).strftime("%d-%m")
#temp_issue_date = datetime.strptime(issue_date, date_format).strftime("%d-%m")

# Выводим введенные данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата создания заметки(День и месяц):", temp_created_date)
print("Дата истечения заметки:", issue_date)
print("Дата окончания заметки(День и месяц):", temp_issue_date)