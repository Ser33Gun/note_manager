Проект "Система управления заметками"

main.py - Не используется, дань уважения ООП:)

Grade 1. Этап 1

Задание 1. 
greetings.py - Изначально просто создаем переменные.
Выводим их на экран.

Задание 2. 
date_changer.py - Изначально создаем переменные, делаем обрезание через [:5]
Модифицировано инициализируем через input().
Обрезание можно делать через формирование типа в datetime
Выводим данные на экран.

Задание 3. 
add_input.py - Инициализация переменных через input()
Обрезание года производится через [:5] при выводе на экран.

Задание 4. 
add_list.py - Копия add_input.py + добавлен список titles для хранения 3 заголовков в виде списка.
Инициализация списка идет через цикл for.
Выводим данные на экран.

Задание 5.
final.py - Собираем все данные в Список. Выводим данные на экран.
Модифицированная версия - Собираем все данные в словарь. Выводим данные на экран.

Grade 1. Этап 2

Задание 6.
add_titles_loop.py - Реализован цикл while для ввода нескольких заголовков.
Остановка цикла по пустой строке. Структурированный вывод на экран.
Модифицированная версия - Повторяющие заголовки не добавляются в список.
Список заголовков выводится поэлементно.

Задание 7.
update_status.py - Реализовано отображение и изменение статуса заметки.
Для изменения принимается только статус из списка (ввод может быть словом или цифрой).

Задание 8.
check_deadline.py - Пользователь вводит дату ДД-ММ-ГГГГ (или другой вариант через дефис).
Программа считывает удобный вариант и переводит его в формат datetime.
Затем сравнивает с текущей датой, и выводит сообщение о разнице.
Реализовал через 2 функции. В одной попробовал использовать try/except.
	create_date - перевод введенной строки в дату.
	get_date - сравнение с текущей датой и возврат переменной для присваивания.

Задание 9.
multiple_notes.py - Реализовано создание нескольких заметок, каждая сохраняется в виде словаря.
Использованы отдельные функции:
	create_date - перевод введенной строки в дату.
	get_date - сравнение с текущей датой и возврат переменной для присваивания.
	get_titles - сбор нескольких заголовков, одинаковые не собираются.
	get_status - ввод статуса
	create_one_note - создание заметки и ее возрат.
	add_note - добавляет запись в общий спиок, подбирая минимальный возможный ID.
	print_note - форматированный вывод заметки.
Модифицировано - добавлено ID для каждой заметки.

Задание 10.
delete_note.py - Копия предыдущего задания + реализация удаления заметки.
Дополнительно сделал первую версию меню.
	delete_note - удаляет все записи одного пользователя или заметки всех пользователей с определенным заголовоком.
		Перед удалением выводит информацию об удаляемой заметке.

Grade 1. Этап 3

Задание 11.
create_note_function.py - Копия предыдущего задания + изменения и дополнения.
	Выбор статуса из кортежа был реализован ранее в update_status.py
	get_titles - Удалена, т.к используется только один заголовок.
	get_date - Изменена, добавлена проверка на пустую строку. 
		В случае даты начала указывается текущая дата, в случае даты истечения - текущая + 7 дней.
	get_input - Функция для ввода общих данных, с проверкой на пустую строку (просит ввести повторно).
	create_one_note - использует get_input там, где может.
	delete_note - добавил подфункцию фактического удаление заметки (sub_del)
	print_note переименовал в display_note

Задание 12.
update_note_function.py - Копия предыдущего задания + изменения и дополнения.
	get_date - Модифицированно для проверки даты начала (не больше даты окончания) 
		и окончания (не меньше текущей)+ форматированный вывод.
	get_status - Форматированный вывод
	update_note - Обновление заявки. Сначала запрашивается номер заявки, затем индекс ключа из кортежа.
		Затем запрашиваются данные, потом система требует подтвержения изменений по слову Да.
		Выводятся изменения и затем система запрашивает хочет ли пользователь внести еще измения в эту заметку.

Задание 13.
display_notes_function.py
	display_notes(notes) - Скопировал предыдущые задания + внес изменения.
	notes теперь список, хранящий словари заметок. Переписал все функции под новый тип. 
	Добавил цветовой вывод с помощью colorama.
		Белый - для пунктов списков (Меню, Ключи);
		Желтый - для запроса ввода информации, например логина;
		Голубой - Для ввода подтвержения;
		Зеленый - Для успешного выполнения;
		Красный - Для отказа выполнения;
		Синий и фиолетовый - для Вывода информации.
	display_notes - Вывод в табличном формате. В случае вывода одной заметки (изменение, удаление) - полный вывод.
		В случае выбора из меню - возможен сокращенный вывод (ID, логин, заголовок).
		Если список заметок содержит больше 5 заметок на странице, то выводится 5 элементов, 
		а потом просьбу ввести Enter для следующих 5 элементов.
		
Задание 14.
	search_notes_function.py - Скопировал из задания 13 функцию display_notes.
	search_logic - возвращает bool из условия совпадения.
	search_notes_function - Функция поиска. Логика поиска в функции search_logic, решил пока не улучшать.
	Возможен поиск с нечувствительностью к регистру. При отсутствии ключевых слов - сообщение об ошибке.
	Поиск по дате по умолчанию не предусмотрен.
	
Задание 15.
menu.py - Меню выделено в отдельную функцию. 
	Кроме того скорректировал файлы display_notes_function.py, search_notes_function.py, update_note_function.py,
	create_note_function.py и delete_note.py на наличие только необходимой в них функции.
	В каждой функции импортируется нужная зависимость.

Grade 1. Этап 4
Все задания хранятся в файле work_with_file.py

Задание 16.
	Сохранение заметок в файл.
	Написана функция save_notes_to_file(notes, file_name). Перезаписывает данные файла, записывая список заметок в текстовом формате YAML.
	Файл создается, если его не существует. Данные в файле перезаписываются при каждом вызове функции.

Задание 17.
	Загрузка заметок из файла
	Написана функция load_notes_from_file(file_name).
	Читает заметки из текстового файла в формате YAML. Преобразует данные в список словарей.
	Обрабатывает отсутствие файла: создаёт пустой файл и сообщает пользователю. Работает корректно даже с пустым файлом.

Задание 18.
	Обработка ошибок при работе с файлами
	Добавлена обработка ошибок в функции.
		Если файл отсутствует: Создается новый файл и Выводит сообщение пользователю, затем завершает функцию.
		Если файл повреждён или данные некорректны: Выводит сообщение пользователю, затем завершает функцию.
		Если возникают другие ошибки (например, отсутствие прав): Выводит сообщение пользователю, затем завершает функцию.
		
Задание 19.
	Добавление данных в файл.
	Написана функция append_notes_to_file(notes, file_name).
	Добавляет новые заметки в существующий файл, сохраняя старые данные.
	Новые заметки добавляются в конец файла. Старые данные остаются неизменными. Файл создаётся автоматически, если он не существует.

Задание 20.
	Выбор формата файла.
	Написана функция save_notes_json(notes, file_name).
	Сохраняет список заметок в формате JSON. Записывает данные с отступами (indent=4) для удобства чтения.
	Написана функция load_notes_json(file_name).
	Считывает данные из файла, преобразует в список словарей и возвращает в основную функцию.
	Если файл отсутствует: Создается новый файл и Выводит сообщение пользователю, затем завершает функцию.
	Если файл пуст, повреждён или данные некорректны: Выводит сообщение пользователю, затем завершает функцию.
	
Grade 1. Этап 5

Задание 21.
	Работа с модулями и пакетами.
		Организованы модули data, utils, interface, tests. Перенесена функциональность.
		В каждом модуле создайте файл __init__.py, чтобы модули были распознаны как пакеты.
	
Задание 22.
	Упрощение импорта через пакет.
	В каждом пакете (data, utils, interface) создан __init__.py.
	В него импортированы осноыные функции из файлов модуля.
	
Задание 23.
	Рефакторинг функций в модули.
	Перенесены функции в соответствующие модули. Каждая часть проекта содержит только связанные элементы.
	
Задание 24.
	Создание тестов.
	Создан файл test_function.py с функциональными тестами.
	Написаны тесты для проверки работы ключевых функций:
		Корректность сохранения и загрузки заметок - test_save_and_load_notes
		Валидацию данных - test_create_data, test_get_status, test_create_date, test_generate_unique_id
		Удаление данных - test_delete_data
		Поиск данных - test_search_note
		Отображение и поиск заметок - test_display_notes

Задание 25.
	Создание вспомогательных утилит.
	Добавьте вспомогательные функции для валидации данных:
		validate_date не добавлена, т.к реализуема как часть create_date.
		validate_status не добавлена, т.к реализуема как часть get_status.
		generate_unique_id добавлена, но реализовал не через uuid, а через random.randint(1, 10_000)
		
Grade 1. Этап 6

Задание 26.
	Создание базы данных SQLite.
	Создан файл setup_database.py для работы с БД.
	База данных и таблица успешно создаются.
	Код не вызывает ошибок при повторном выполнении.

Задание 27.
	Сохранение заметок в базу данных
	Реализована функция save_note_to_db, которая сохраняет заметку в базу данных.
	
Задание 28.
	Загрузка заметок из базы данных
	Реализована функция load_notes_from_db, которая загружает все заметки из базы данных.
	Все данные корректно извлекаются из базы.
	Функция создает список заметок в виде словарей, который отправялется в функцию check_exist_notes.
	Там производится поиск ключей, которых еще нет в базе, и вовзврат их в списке.
	Затем этот список расширяет изначально переданный список.