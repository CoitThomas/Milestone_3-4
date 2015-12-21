import math, os

a = input('a:')
b = input('b:')

def calc1(a,b,c,nc=False, logging=True):
	if c:
		return c

	if logging: 
		print "a is ", a
		a = pow(a,2)
	if logging:
		print "b is ", b
		a = pow(a,2)
	c = a + b

	
	c2 = math.sqrt(c)

	if nc:
		c = 2 * c * math.pi
		return c
	return c2

print "The hypotenuse is ", calc1(a,b,None)
