from lib.say_hello import *

# Intended output:
#
# > say_hello("kay")
# => "hello kay"

def test_says_hello_to_given_name():
    result = say_hello("Marty")
    assert result == 'hello Marty'