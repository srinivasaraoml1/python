# This is an exercise on "Reading And Writing Files"

from sys import argv

sript, file_name = argv

print "We're going to erase %r." % file_name
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")

print("Opening the file")
# opens file in write mode
target = open(file_name, 'w')

print("Truncating the file, Goodbye!")
# truncates the opened file uder the file variable 'target'
target.truncate()

print "Now I'm going to ask you for three lines."
# entering the sample text in different lines
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# writing the entered lines in a sequence into the file opened & truncated initially
target.write(line1+"\n")
target.write(line2+"\n")
target.write(line3+"\n")
