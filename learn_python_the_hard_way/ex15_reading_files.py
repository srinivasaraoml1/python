# This is an exercise on "Reading Files"

from sys import argv

sript, file_name = argv

# opens the text file into a file variable 'txt'
txt = open(file_name)

print(type(txt))
print("Here's your file: %r" %file_name)
# reading the file variable 'txt'
print(txt.read())

print "Type the filename again:"
file_again = raw_input("> ")

# opens the text file into a file variable 'txt_again'
txt_again = open(file_again)
# reading the file variable 'txt_again'
print txt_again.read()
