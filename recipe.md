# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

``` python
# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

``` python
def estimate_reading_time(str):
    #parameters:
    #   str: a string containing words.
    #returns:
    #   a string containing an estimate of the reading time for the text given (e.g. "This text will take you approximately 5 minutes and 10 seconds to read.")
    #side effects:
    #   this function has no side effects
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

``` python
"""
Given an empty string
will return a message stating string is empty
"""
# estimate_reading_time('') => 'There is no text in the provided string.'

"""
Given a string of any length
will return a message with an estimate of how long it will take to read at 200wpm in minutes and seconds
"""
# estimate_reading_time('Hello my name is placeholder text.') => 'This text will take you approximately 0 minutes and 3 seconds to read.'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

# Fill out here

Ensure all test function names are unique, otherwise pytest will ignore them!