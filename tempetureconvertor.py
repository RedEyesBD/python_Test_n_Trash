#Fahrenheit to Celsus  and Kelvin Convertor
#Author: Jose Garcia -2.9.12.12 19.1.25.19 8.5.12.12.15!

def f2cConveror (t):
	#print "Converting %.2f Fahrenheit to Celsus" % t
	c = (t - 32) * (5.0 / 9.0)
	return c

def c2kConvertor (t):
	#print "Converting %.2f Celsus to Kelvin" % t testing propuse print.
	k = (t + 273.15)
	return k

print "\nSo want to know something about tempeture?\nFahrenheit is not a popular unit to messuere the tempeture\nFor example:"
fah = input("Enter some F tempeture: ")	
print "That tempetue %.2f Fahrenheit, becomes:\n%.2f Celsus and %.2f Kelvin, those are more common ways to messuere the tempeture" % (fah, f2cConveror(fah), c2kConvertor(f2cConveror(fah)))
