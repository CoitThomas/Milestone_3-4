from hyp1 import assert_and_convert

def test_assert_and_convert():
    assert assert_and_convert(1000) == 1000.0
    assert assert_and_convert(50.0) == 50.0