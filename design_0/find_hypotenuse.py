"""This module prompts a user to enter the lengths of two sides of a
right triangle. Those values are then operated on in order to find the
length of the hypotenuse. A print out of all three sides is then given.
"""

import math

def convert_sides(user_input1, user_input2):
    """convert_sides(unknown, unknown) -> (float, float)

    Take two unknown variables, user_input1 and user_input2, and
    convert both of them to variables of type float. The float()
    function will return a ValueError if user_inputX is something other
    than a number.
    """
    side_a = float(user_input1)
    side_b = float(user_input2)

    return (side_a, side_b)

def assert_positive(number1, number2):
    """assert_positive(float, float) -> none

    Determine if the two numbers given are positive.
    """
    assert number1 > 0.0, "Side 'A' must be positive."
    assert number2 > 0.0, "Side 'B' must be positive."

def get_input():
    """get_input() -> (float, float)

    Instruct and gather user input of two sides of a right triangle.
    """
    print 'Enter the two sides of your right triangle.'
    input_a = raw_input('a:')
    input_b = raw_input('b:')

    side_a, side_b = convert_sides(input_a, input_b)
    assert_positive(side_a, side_b)

    return (side_a, side_b)

def find_hypotenuse(side_a, side_b):
    """find_hypotenuse(float, float) -> float

    Calculate and return the hypotenuse of a right triangle.
    """
    assert_positive(side_a, side_b)

    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))

if __name__ == "__main__":
    (SIDE_A, SIDE_B) = get_input()
    HYPOTENUSE = find_hypotenuse(SIDE_A, SIDE_B)
    print """
a is %.2f
b is %.2f
The hypotenuse is %.2f""" % (SIDE_A, SIDE_B, HYPOTENUSE)
