from lib.grammar_stats import * 

"""
After checking some strings for grammar
Can return percentage of checked strings that satisfied criteria
"""
def test_return_correct_percentage():
    grammar_checker = GrammarStats()
    grammar_checker.check('does not begin with capital.')
    grammar_checker.check('Correct sentence structure.')
    grammar_checker.check('Whoops, forgot to finish with punctuation')
    grammar_checker.check('Remembered this time, yay.')
    result = grammar_checker.percentage_good()
    assert result == 50