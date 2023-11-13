from lib.count_words import *

# A function called count_words
# that takes a string as an argument 
# and returns the number of words in that string.

"""
When given empty string, returns 0
"""
def test_empty_string_returns_0():
    result = count_words('')
    assert result == 0

"""
When given a string of 9 words, returns 9
"""
def test_returns_10_when_given_10_word_string():
    result = count_words('This is an example string to test a function.')
    assert result == 9