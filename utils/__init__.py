# Кортеж с ключами.
tuple_keys = ("Id", "Username", "Title", "Content", "Status", "Created_date", "Issue_date")

from utils.create_note_function import get_input, get_status, get_date, add_note
from utils.update_note_function import check_exist_notes, update_note
from utils.search_notes_function import search_notes, display_searching_notes
from utils.delete_note_function import delete_note

