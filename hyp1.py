import math, os

a = input('a:')
b = input('b:')

def find_hypotenuse(a,b):
	return math.sqrt(pow(a,2)+pow(b,2))
	
def print_hypotenuse(a,b):
		c = find_hypotenuse(a,b)
		print "a is", a
		print "b is", b
		print "The hypotenuse is", c

find_hypotenuse(a,b)
print_hypotenuse(a,b)