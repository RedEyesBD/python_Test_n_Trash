# Area of a Triangle and a Rectangle

from sys import argv

script, base, side = argv #values as a string, need to convert them first

print "\tAreas\n\n**Triangle**\n"
area = (float(base) * float(side))*0.5
print "\n**Total Area**\n%.2f" % area + " square mts"

print "\tAreas\n\n**Rectangle**\n"
base = float(raw_input("Input the base: ")) #converting string to float
lado = float(raw_input("Input the side: "))

area = base * side

print "\n**Total Area**\n%.2f" % area + " square mts"