from hyp1 import find_hypotenuse

def test_find_hypotenuse():
    assert find_hypotenuse(3, 4) == 5
    assert 5.7 < find_hypotenuse(3.5, 4.5) < 5.71
