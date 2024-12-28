from datetime import datetime

# Перевод строки в дату, если строка дана в одном из 6 форматов.
def create_date (str_date):
    formated_date = ""
    date_formats = ("%Y-%m-%d", "%Y-%d-%m", "%m-%d-%Y", "%m-%Y-%d", "%d-%m-%Y", "%d-%m-%Y")
    for i in date_formats:
        try:
            formated_date = datetime.strptime(str_date, i).date()
        except ValueError:
            pass
    if formated_date == "":
        print("Дата задачи введена некорректно! Повторите ввод.")
        return 1
    return formated_date

# Сравнение даты + возврат даты.
def get_date (word):
    date_today = datetime.today().date()
    str_date = input("Введите дату " + word + " задачи через дефис, например 31-12-2024:")
    formated_date = create_date(str_date)
    while formated_date == 1:
        formated_date = create_date(input("Введите дату" + word + "задачи через дефис, например 31-12-2024:"))
    temp_days = int((date_today - formated_date).days)
    if  temp_days > 0:
        print("Дата " + word + " задачи началась " + str(temp_days) + "дня назад.")
    elif temp_days == 0:
        print("Дата " + word + " задачи сегодня!")
    elif temp_days < 0:
        print("Дата " + word + " задачи через " + str(abs(temp_days)) + " дня.")
    return formated_date

# Значения дат
start_date = get_date("начала")
deadline_date = get_date("конца")

print(start_date)
print(deadline_date)