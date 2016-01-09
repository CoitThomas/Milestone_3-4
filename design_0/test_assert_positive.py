"""Unit test which verifies the passage of two positive floating point
numbers through assert_positive(float1, float2)."""

from find_hypotenuse import assert_positive

def test_assert_positive():
    """test_assert_positive() -> none

    Call assert_positive(float, float) and verify that two positive
    floating point numbers can pass through.
    """
    assert assert_positive(45.6, 1234.667) is None
    assert assert_positive(0.1111, 100000.2) is None
