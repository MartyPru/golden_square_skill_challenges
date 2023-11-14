from lib.contains_todo import *

"""
When given empty string, returns message stating string is empty.
"""
# contains_todo('') => 'Please provide some text.'
def test_returns_message_when_given_empty_string():
    result = contains_todo('')
    assert result == 'Please provide some text.'

"""
When given string with '#TODO' somewhere in the string, returns True
"""
# contains_todo('Walk the dog #TODO') => True
def test_returns_true_when_text_contains_todo():
    result = contains_todo('Walk the dog #TODO')
    assert result == True

"""
When given string without '#TODO' present, returns False
"""
# contains_todo('Do the laundry') => False
def test_returns_false_when_text_does_not_contain_todo():
    result = contains_todo('Do the laundry')
    assert result == False

