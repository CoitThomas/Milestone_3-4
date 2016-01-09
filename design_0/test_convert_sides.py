"""Unit test which verifies the conversion of two user-given-numbers to
two floating-point-numbers.
"""

from find_hypotenuse import convert_sides

def test_convert_sides():
    """test_convert_sides() -> none

    Test convert_sides(user_input1, user_input2) to confirm that the
    input given is properly converted to floating point numbers.
    """
    assert convert_sides(1000, 23) == (1000.0, 23.0)
    assert convert_sides(50.222222, 100.1) == (50.222222, 100.1)
    assert convert_sides(5, 6.7) == (5.0, 6.7)
    assert convert_sides(2.3, 4) == (2.3, 4.0)
