#Integrated tests for ultra_diary class system
from lib.ultra_diary import *

"""
After being given diary entries
can return all entries in readable format
"""
def test_returns_diary_entries():
    entry_1 = DiaryEntry('Entry 1', 'This is some content in the first entry.')
    entry_2 = DiaryEntry('Entry 2', 'This is some content in the second entry. This one is longer than the other two.')
    entry_3 = DiaryEntry('Entry 3', 'This is some content in the third entry.')
    diary = UltraDiary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.read() == "Entry 1: This is some content in the first entry. \n\nEntry 2: This is some content in the second entry. This one is longer than the other two. \n\nEntry 3: This is some content in the third entry. \n\n"


"""
After beign given diary entries
can return entries that can be read in given time
based on reading speed in wpm and time in minutes
"""
def test_returns_diary_entries_to_read_in_time():
    entry_1 = DiaryEntry('Entry 1', 'This is some content in the first entry.')
    entry_2 = DiaryEntry('Entry 2', 'This is some content in the second entry. This one is longer than the other two.')
    entry_3 = DiaryEntry('Entry 3', 'This is some content in the third entry.')
    diary = UltraDiary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.entries_for_reading_time(10, 1) == "In the time you have, you can read any of the following entries: \n\n      Entry 1: This is some content in the first entry. \n\n      Entry 3: This is some content in the third entry. \n\n"


"""
After being given diary entries containing phone numbers
can return a list of phone numbers
"""
def test_returns_list_of_numbers():
    entry_1 = DiaryEntry('Entry 1', 'This is some content in the first entry. Here is a fake phone number 09685746354.')
    entry_2 = DiaryEntry('Entry 2', 'This is some content in the second entry. This one is longer than the other two. Not much longer, but it is longer. Here is a number, but it is not a phone number 0845.')
    entry_3 = DiaryEntry('Entry 3', 'This is some content in the third entry. Another fake phone number 07968574637')
    diary = UltraDiary()
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.find_numbers() == ['09685746354','07968574637']


"""
After being given tasks to keep track of
can return list of incomplete tasks
"""
def test_returns_list_of_incomplete_tasks():
    task_1 = ToDo('Walk the dog')
    task_2 = ToDo('Wash the dishes')
    diary = UltraDiary()
    diary.todo_list.add(task_1)
    diary.todo_list.add(task_2)
    assert diary.todo_list.incomplete() == ['Walk the dog','Wash the dishes']


"""
After being told a task is complete,
correctly adds it to complete list and returns list of completed tasks when requested
"""
def test_returns_list_of_complete_tasks():
    task_1 = ToDo('Walk the dog')
    task_2 = ToDo('Wash the dishes')
    diary = UltraDiary()
    diary.todo_list.add(task_1)
    diary.todo_list.add(task_2)
    task_1.mark_complete()
    assert diary.todo_list.complete() == ['Walk the dog']