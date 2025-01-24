import unittest
from datetime import datetime

import data
import interface
import utils


class TestNoteManager(unittest.TestCase):
    def test_save_and_load_notes(self):
        notes = [{'username': 'Test', 'title': 'Test Note'}]
        data.save_notes_json(notes, 'test.json')
        loaded_notes = data.load_notes_json('test.json')
        self.assertEqual(notes, loaded_notes)

    # Тест создания значений.
    def test_create_data(self):
        validate_test = [{
            "Id": 1,
            "Имя": "Алексей",
            "Заголовок": "Список",
            "Описание": "Купить",
            "Статус": "Новая",
            "Дата начала": "2025-01-10",
            "Дата истечения": "2025-01-17"
        }]
        notes = []
        utils.create_note_function.add_note(notes)

        # Проверка добавления записи проводится поэлементно, т.к ID уникален.
        for i in range(1, len(validate_test)):
            self.assertEqual(notes[i], validate_test[i])

    def test_get_status(self):
        #Проверка статуса
        self.assertEqual("Новая", utils.create_note_function.get_status())

    def test_create_date(self):
        message = "Test value is none."
        # Проверка генерации даты.
        self.assertEqual(datetime.strptime("2025-01-10", "%Y-%m-%d").date(), utils.create_note_function.get_date("начала"),)
        self.assertIsNotNone(utils.create_note_function.create_date("2025-01-10"))
        # Пример неудачного теста
        #self.assertIsNotNone(utils.create_note_function.create_date("sometext"), message)

    # Тест удаления заявки
    def test_delete_data(self):
        notes = []
        delete_test = [{
            "Id": 1,
            "Имя": "Алексей",
            "Заголовок": "Список покупок",
            "Описание": "Купить продукты на неделю",
            "Статус": "Новая",
            "Дата начала": "2025-01-10",
            "Дата истечения": "2025-01-17"
        }]
        rf = utils.check_exist_notes(notes, data.load_notes_json('../ex.json'))
        if rf:
            notes.extend(rf)
        utils.delete_note()

    # Тест поиска заявки.
    def test_search_note(self):
        notes = []
        search_test = [{
            "Id": 1,
            "Имя": "Алексей",
            "Заголовок": "Список покупок",
            "Описание": "Купить продукты на неделю",
            "Статус": "Новая",
            "Дата начала": "2025-01-10",
            "Дата истечения": "2025-01-17"
        }]
        rf = utils.check_exist_notes(notes, data.load_notes_json('../ex.json'))
        if rf:
            notes.extend(rf)
        self.assertEqual(search_test, utils.search_notes(notes))

    # Тест отображения заявок.
    def test_display_notes(self):
        notes = []
        loaded_notes = data.load_notes_json('../ex.json')
        rf = utils.check_exist_notes(notes, data.load_notes_json('../ex.json'))
        if rf:
            notes.extend(rf)
        self.assertEqual(notes, loaded_notes)
        interface.display_note(notes)

    # Тест генерации уникального ИД.
    def test_generate_unique_id(self):
        id1 = utils.create_note_function.generate_unique_id([])
        id2 = utils.create_note_function.generate_unique_id([])
        self.assertNotEqual(id1, id2)

if __name__ == '__main__':
    unittest.main()