# Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

``` python
#As a user
#So that I can keep track of my tasks
#I want to check if a text includes the string #TODO.
```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

``` python
def contains_todo(str):
    #parameters:
    #   a string containing words
    #returns:
    #   a boolean, 'True' if string contains '#TODO'
    #   'False' if string does not contain '#TODO'
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

``` python
"""
When given empty string, returns message stating string is empty.
"""
# contains_todo('') => 'Please provide some text.'

"""
When given string with '#TODO' somewhere in the string, returns True
"""
# contains_todo('Walk the dog #TODO') => True

"""
When given string without '#TODO' present, returns False
"""
# contains_todo('Do the laundry') => False


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!