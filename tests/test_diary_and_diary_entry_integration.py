from lib.diary import *
from lib.diary_entry import *

"""
Given several diary entries
can return a list of entries
"""
def test_returns_list_after_several_diary_entries():
    entry_1 = DiaryEntry('Title 1', 'This is the first entry of the diary.')
    entry_2 = DiaryEntry('Title 2', 'This is the second entry in the diary.')
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == ['Title 1', 'Title 2']


"""
With several entries in list
Can return total word count of entries
"""
def test_returns_total_word_count_of_entries():
    entry_1 = DiaryEntry('Title 1', 'This is the first entry of the diary.')
    entry_2 = DiaryEntry('Title 2', 'This is the second entry in the diary.')
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 20


"""
With several entries in list
Can give an estimate of reading time in minutes for entire diary
"""
def test_returns_estimate_of_reading_time():
    entry_1 = DiaryEntry('Title 1', 'This is the first entry of the diary.')
    entry_2 = DiaryEntry('Title 2', 'This is the second entry in the diary.')
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(10) == 2


"""
Given a reading speed and an amount of time
Can return appropriate entries to be read in that time
"""
def test_selects_appropriate_entries_for_reading_speed_and_time():
    entry_1 = DiaryEntry('Title 1', 'This is the first entry of the diary.')
    entry_2 = DiaryEntry('Title 2', 'This is the second entry in the diary. Some extra words.')
    entry_3 = DiaryEntry('Title 3', 'This is the third diary entry. It is longer and cannot be read as fast as the first two.')
    diary = Diary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_best_entry_for_reading_time(15, 1) == ['Title 2']