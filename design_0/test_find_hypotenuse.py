"""Unit test which verifies the correct calculation of the hypotenuse
of the right triangle.
"""

from find_hypotenuse import find_hypotenuse

def test_find_hypotenuse():
    """test_find_hypotenuse() -> none

    Call find_hypotenuse(float, float) to test that the resulting
    calculation is correct.
    """
    assert find_hypotenuse(3, 4) == 5
    assert 5.7 < find_hypotenuse(3.5, 4.5) < 5.71
