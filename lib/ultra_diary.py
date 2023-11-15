from lib.diary_entry import *
from lib.todo import *
from lib.todo_list import *
import re

class UltraDiary:
    def __init__(self):
        self._entries = []
        self.todo_list = TodoList()

    def add(self, entry):
        self._entries.append(entry)

    def read(self):
        new_string = ''
        for k in self._entries:
            new_string += f"{k.title}: {k.contents} \n\n"
        return new_string

    def entries_for_reading_time(self, wpm, minutes):
        words_can_read = wpm * minutes
        valid_entries = []
        for entry in self._entries:
            if entry.count_words() <= words_can_read:
                valid_entries.append(entry)
        return_string = f"In the time you have, you can read any of the following entries: \n\n"
        for entry in valid_entries:
            return_string += f"      {entry.title}: {entry.contents} \n\n"
        return return_string
    
    def find_numbers(self):
        all_matching = []
        for entry in self._entries:
            matching = re.findall(r'\d{11}', entry.contents)
            if len(matching) > 0:
                all_matching += matching
        return all_matching