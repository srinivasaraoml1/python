# This is an exercise on "Reading And Writing Files"

from sys import argv

sript, file_name = argv

print "We're going to erase %r." % file_name
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

print("Opening the file")
target = open(file_name, w)

print("Truncating the file, Goodbye!")
target.truncate()

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
