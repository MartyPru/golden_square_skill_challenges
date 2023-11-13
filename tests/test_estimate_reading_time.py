from lib.estimate_reading_time import *

"""
Given an empty string
will return a message stating string is empty
"""
# estimate_reading_time('') => 'There is no text in the provided string.'
def test_returns_error_message_if_given_empty_string():
    result = estimate_reading_time('')
    assert result == 'There is no text in the provided string.'

"""
Given a string of any length
will return a message with an estimate of how long it will take to read at 200wpm in minutes and seconds
"""
# estimate_reading_time('Hello my name is placeholder text.') => 'This text will take you approximately 0 minutes and 3 seconds to read.'
def test_returns_estimated_reading_time_of_1_min_for_string_of_200_words():
    result = estimate_reading_time('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam a nulla ultrices, sodales eros vitae, eleifend sapien. Cras in porttitor lectus, eget elementum mauris. Vestibulum at efficitur ex, vitae condimentum lacus. Suspendisse eu mi mauris. Quisque faucibus arcu vitae hendrerit varius. Fusce cursus neque non convallis bibendum. Nunc auctor, tellus ac condimentum tristique, quam lorem fringilla odio, non pharetra dolor ligula ut ex. Nulla nec lorem pharetra ante ultricies eleifend eu nec magna. Donec porttitor nisi nec mauris viverra mollis. Etiam mauris nisl, condimentum sit amet luctus in, ultrices eget ligula. Praesent eget nulla id magna elementum consectetur id sit amet quam. Aenean vulputate odio in pretium facilisis. Nam ac sollicitudin sem, non scelerisque felis. Nam sit amet urna dignissim erat fringilla malesuada ac sit amet tortor. Sed sodales libero vel diam bibendum, sed ultricies eros aliquam. Suspendisse efficitur accumsan turpis lobortis dictum. Maecenas hendrerit orci elit, vitae eleifend libero condimentum ac. Donec porttitor, magna eget aliquam malesuada, nunc urna malesuada mauris, ac blandit arcu libero at massa. Fusce accumsan, mi id vehicula vestibulum, est orci varius velit, vitae euismod enim massa sit amet erat. Proin et diam quis lacus congue pulvinar id et dui. Quisque fermentum condimentum eros luctus.')
    assert result == 'This text will take you approximately 1 minute(s) and 0 second(s) to read.'