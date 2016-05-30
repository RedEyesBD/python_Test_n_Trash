# An RPG data capture
#Author: Jose Garcia -25.5.19 9 4.15 12.9.11.5 16.15.11.5.13.15.14
print "\t***Welcome to Eternal Journy***\nGood Day, Sir?, Mistress?, soon we'll see, now please follow my lead and answer my questions\nAre you a Lord or a Lady?"
ans = raw_input("Enter 1 for Lord or 2 for Lady: ")
if ans == "1":
	print "God bless you, my Lord!"
	sex = "Lord"
	flag = True
elif ans == "2":
	print "God bless you, my Lady!"
	sex = "Lady"
	flag = True
else:
	print "So we have a smart one, well now you're a pig, next time just follow my lead!"
	sex = "Pig"
	flag = False

print "Now my %s, What is your name?" % sex
name = raw_input("Enter your name: ")
short_name = sex + " " + name[0] + "."
if (sex == "Lord" or sex == "Lady"):
	print "\nVery Well %s %s, but from now you will be know as %s, long life %s!!!\nThe story goes on... " % (sex, name, short_name, short_name)
else:
	print "\nSo do you like your name?, don't you %s!!!, i'll give you one more chance, just tell me WHAT ARE YOU!" % short_name


if flag == False:
	ans = raw_input("Just press 1 or 2: ")
if (ans == "1" and flag == False):
	print "See it wasn't that dificult, Bless thee Lord!!"
	sex = "Lord"
	short_name = sex + " " + name[0] + "."
	print "\nNow I clam that the Pig has become %s!!! all hail %s!!!\nThe story goes on..." % (short_name, short_name)
elif (ans == "2" and flag == False):
	print "See it wasn't that dificult, Bless thee Lady!!"
	sex = "Lady"
	short_name = sex + " " + name[0] + "."
	print "\nNow I clam that the Pig has become %s!!! all hail %s!!!\nThe Story goes on..." % (short_name, short_name)
else:
	if (sex == "Pig" and flag == False):
		print "Fine, it's that the way you want the things, it's fine, I clam, today the dinner is Pig!!!\n***GAME OVER***\n\tBad End 001: Bacon"