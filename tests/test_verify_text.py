from lib.verify_text import *

"""
If given empty string, return string stating 'Invalid - empty string'.
"""
def test_returns_invalid_with_empty_string():
    result = verify_text('')
    assert result == 'Invalid - empty string.'


"""
If given string starting with lowercase letter, return string stating 'Invalid - does not begin with capital letter.'
"""
def test_returns_invalid_with_lowercase_start():
    result = verify_text('hello.')
    assert result == 'Invalid - does not begin with capital letter.'


"""
If given string without ending punctuation, returns string stating 'Invalid - does not have ending punctuation'.
"""
def test_returns_invalid_with_no_punctuation():
    result = verify_text('Hello')
    assert result == 'Invalid - does not have ending punctuation.'


"""
If given string meeting criteria, returns 'Valid - string meets criteria.'
"""
def test_returns_valid_with_valid_string():
    result = verify_text('Hi this is a test string.')
    assert result == 'Valid - string meets criteria.'