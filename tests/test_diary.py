from lib.diary import *

"""
If no entries in diary
when asked to count words
should return 0
"""
def test_returns_0_word_count_when_no_entries():
    diary = Diary()
    assert diary.count_words() == 0


"""
If no entries in diary
when asked to return list of entries
should return empty list
"""
def test_returns_empty_list_when_no_entries():
    diary = Diary()
    assert diary.all() == []


"""
If no entries in diary
when asked to calculate reading time
returns 0
"""
def test_returns_0_reading_time_when_no_entries():
    diary = Diary()
    assert diary.reading_time(10) == 0


"""
If no entries in diary
when asked to find best entry for reading time
returns empty list
"""
def test_returns_empty_list_for_best_entry_when_no_entries():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(10, 2) == []