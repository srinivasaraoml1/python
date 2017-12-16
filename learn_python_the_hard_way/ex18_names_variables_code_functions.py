# This is an exercise on "Names, Variables, Code, Functions"

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg):
    print ("arg: %r" % (arg))

# this one does nothing
def print_none():
    print("I got nothin")

print_two(1,2)
print_two_again(1,2)
print_one(2)
print_none()
