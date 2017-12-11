# Exercise - 5 : More Variables and Printing
#

my_name = 'Srinivas'
my_age = 25 # not a lie
my_height = 70 # inches
my_weight = 180 # lbs
my_eyes = 'black'
my_teeth = 'brown'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get this exactly right
print "If I add %d, %d and %d I get %d." % (my_age, my_height, my_weight, my_age+my_height+my_weight)
