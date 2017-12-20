# This is an exercise on "Reading Files"

# Format-1
# Reading file and printing data in a single instance
data = open("resources/sample.txt", 'r')
print(data.read())

# Format-2
data = open("resources/sample.txt", 'r')
dao = data.readline()
print(dao)

# Format-3
data = open("resources/sample.txt", 'r')
da = data.readlines()
# Read lines returns the lines in a list with a new line tag at the end
# ['This is a sample text file\n', "Basically it's trash\n", 'But we are still reading it...']
print(da)

for line in da:
    print(line)

# Format-4
# handle = open("resources/sample.txt", 'r')
# while True:
#     mong = handle.read(1024)
#     print(mong)
#     if not data:
#         break

# Format-5
# Reads the binary files such as pdf and prints them
read_binary = open("resources/python_101.pdf", 'rb')
print(read_binary.readline())

# Format-5
with open("resources/sample.txt") as handles:
    # returns a file
    print(handles)
    for line in handles:
        print(line)

# Common Exceptions found in reading files
try:
    handles = open("resources/sample1.txt")
    for line in handles:
        print(line)
except:
    print("An exception has occured")
finally:
    handles.close()