# This is an exercise on "More Variables and Printing"

name = 'Zed A. Shaw'
age=35#notalie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print"IfIadd%d,%d,and%dIget%d."%(age, height, weight, age + height + weight)
