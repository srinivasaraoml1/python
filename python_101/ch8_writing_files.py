# This is an exercise on "Writing Files"

data = open("resources/output.txt", 'w')
data.write("This is a sample data for writing text files.\n")
data.write("The purpose of this line is more or less the same..\n")
data.write("Hi der, this line's purpose is to say that this is the last line...\n")
data.close()