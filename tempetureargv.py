#Fahrenheit to Celsus and Kelvin Convertor
#Author: Jose Garcia -9.6 25.15.21 1.18.5 18.5.1.12.25 4.5.3.15.4.9.14.7 20.8.9.19 9'12.12 7.9.22.5 25.15.21 1 19.14.1.3.11!
# What if we use some argv parameters?.
#hola -
from sys import argv

script, temp = argv 

def f2cConveror (t):
	# Converting from Fahrenheit to Celsus
	c = (t - 32) * (5.0 / 9.0)
	return c

def c2kConvertor (t):
	# Converting from Celsus to Kelvin
	k = (t + 273.15)
	return k

print """
You know what the argv is for, do you?
Well if you can read this you should :-)
Let's see those results!!!
Fahrenheit: %.2f
Celsus: %.2f
Kelvin: %.2f
""" % (float(temp), f2cConvertor(float(temp)), c2kConvertor(f2cConvertor(float(temp))))
