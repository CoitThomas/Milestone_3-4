"""Unit test which varifies the conversion of a user-given-number to a
floating-point-number.
"""

from find_hypotenuse import convert_and_assert

def test_convert_and_assert():
    """test_convert_and_assert() -> none

    Call convert_and_assert(user_input) to test that the input was
    properly converted to a floating point number.
    """
    assert convert_and_assert(1000) == 1000.0
    assert convert_and_assert(50.222222) == 50.222222
