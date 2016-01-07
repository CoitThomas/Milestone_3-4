"""This module prompts a user to enter the lengths of two sides of a
right triangle. Those values are then operated on in order to find the
length of the hypotenuse. A print out of all three sides is then given.
"""

import hyp1

(SIDE_A, SIDE_B) = hyp1.get_input()
HYPOTENUSE = hyp1.find_hypotenuse(SIDE_A, SIDE_B)
print """
a is %.2f
b is %.2f
The hypotenuse is %.2f""" % (SIDE_A, SIDE_B, HYPOTENUSE)
