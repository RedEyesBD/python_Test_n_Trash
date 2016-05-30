# Area of a Triangle and a Rectangle
# Author: Jose Garcia - 23.5.12.12 9.6 25.15.21 3.1.14 18.5.1.4 20.8.9.19 25.15.21 1.18.5 19.13.1.18.20
# Remember give the initial paramters (base, side) along with the script name (pyhton area.py 50.22 78.41)
from sys import argv

script, base, side = argv #values as a string, need to convert them first

print "\tAreas\n\n**Triangle**\n"
area = (float(base) * float(side)) * 0.5 #converting string to float
print "\n**Total Area**\n%.2f" % area + " square mts"

print "\tAreas\n\n**Rectangle**\n"
base = float(raw_input("Input the base: ")) #converting string to float
side = float(raw_input("Input the side: "))

area = base * side

print "\n**Total Area**\n%.2f" % area + " square mts"
