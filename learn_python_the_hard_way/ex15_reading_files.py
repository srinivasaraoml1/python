# This is an exercise on "Reading Files"

from sys import argv

sript, file_name = argv

txt = open(file_name)

print("Here's your file: %r" %file_name)
print(txt.read())

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()
