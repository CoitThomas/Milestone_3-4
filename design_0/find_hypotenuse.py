"""This module prompts a user to enter the lengths of two sides of a
right triangle. Those values are then operated on in order to find the
length of the hypotenuse. A print out of all three sides is then given.
"""

import math

def convert_and_assert(user_input):
    """convert_and_assert(unknown) -> float

    Take an unknown variable, 'user_input', and convert it to a
    variable of type float. The float() function will return a
    ValueError if the 'user_input' is something other than a number.
    Then assert 'convert' is positive and return it.
    """
    convert = float(user_input)
    assert convert > 0.00, "Input must be a positive number."

    return convert

def get_input():
    """get_input() -> (float, float)

    Instruct and gather user input of two sides of a right
    triangle.
    """
    print 'Enter the two sides of your right triangle.'
    input_a = raw_input('a:')
    input_b = raw_input('b:')

    side_a = convert_and_assert(input_a)
    side_b = convert_and_assert(input_b)

    return (side_a, side_b)

def find_hypotenuse(side_a, side_b):
    """find_hypotenuse(float, float) -> float

    Calculate and return the hypotenuse of a right triangle.
    """
    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))

if __name__ == "__main__":
    (SIDE_A, SIDE_B) = get_input()
    HYPOTENUSE = find_hypotenuse(SIDE_A, SIDE_B)
    print """
a is %.2f
b is %.2f
The hypotenuse is %.2f""" % (SIDE_A, SIDE_B, HYPOTENUSE)
