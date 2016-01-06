from math import sqrt, pow

def assert_and_convert(user_input):
    """assert_and_convert(unknown) -> float
    
    Assert that the input given by the user is appropriate. Convert
    that input into a float. Return the input.
    """
    assert (isinstance(user_input, float) or
            isinstance(user_input, int)), "Value must be of type int or type float."
    assert user_input > 0, "Value should be greater than zero."
    if isinstance(user_input, int):
        float(user_input)
    return user_input

def get_input():
    """get_input() -> (float, float)

    Instruct and gather user input of two sides of a right 
    triangle.
    """
    print "Enter the two sides of your right triangle."
    a = input('a:')
    a = assert_and_convert(a)
    b = input('b:')
    b = assert_and_convert(b)
    return (a, b)

def find_hypotenuse(a, b):
    """find_hypotenuse(float, float) -> float

    Calculate and return the hypotenuse of a right triangle.
    """
    return math.sqrt(pow(a, 2) + pow(b, 2))

def print_hypotenuse(a, b, c):
    """print_hypotenuse(float, float, float) -> none

    Print out the values of sides 'a' and 'b' of the triangle and
    its corresponding hypotenuse.
    """
    print "a is", a
    print "b is", b
    print "The hypotenuse is", c

(a, b) = get_input()
c = find_hypotenuse(a, b)
print_hypotenuse(a, b, c)