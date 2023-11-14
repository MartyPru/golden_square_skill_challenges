from lib.diary_entry import *
"""
After being given diary entry with title
can format entry and estimate reading time for diary
"""
def test_diary_entry_reading_estimate():
    diary = DiaryEntry('Test', 'This is a simple test of the class.')
    result = diary.reading_time(9)
    assert result == 1


"""
After being given diary entry
can return chunks that can be read in specified number of minutes based on specified reading speed
each chunk should pick up from where previous chunk left off
"""
def test_diary_reading_chunk():
    diary = DiaryEntry('Test', 'This is a simple test of the class.')
    diary.reading_chunk(3, 1)
    diary.reading_chunk(3, 2)
    result = diary.reading_chunk(3, 1)
    assert result == 'Test: This is'