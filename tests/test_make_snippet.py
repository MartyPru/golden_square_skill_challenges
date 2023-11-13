from lib.make_snippet import *

# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

"""
If given string less than 5 words, returns string.
"""
def test_returns_string_given():
    result = make_snippet('hello')
    assert result == 'hello'


"""
If given string of five words, returns string
"""
def test_returns_first_five_words():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'


"""
If given string longer than 5 words, returns first five words with '...' appended.
"""
def test_returns_five_words_with_ellipses():
    result = make_snippet('The quick brown fox jumps over the lazy dog.')
    assert result == 'The quick brown fox jumps...'