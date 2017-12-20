# This is an exercise on "Handling Exceptions"

# Bare excepts: It doesn't mention which error has to be excepted

try:
    print(1 // 0)
except:
    print("Zero Division Error, You cannot divide by zero")

try:
    my_dict = {"a":"1", "b":"2", "c":"3"}
    print(my_dict["d"])
except:
    print("Error has occured")

# Proper way to write an exception mentioned above is
try:
    my_dict = {"a":"1", "b":"2", "c":"3"}
    print(my_dict["d"])
except KeyError:
    print("Key Error has occured")
except:
    print("Some other error has occured")

# Using finally statement in conjuction with try block
try:
    print(1 // 0)
except:
    print("Zero Division Error, You cannot divide by zero")
finally:
    print("The finally block has been executed")

# Using the try, except, else instead of the finally block
try:
    print(1 // 1)
except:
    print("Zero Division Error, You cannot divide by zero")
else:
    print("Exception has not occured")

# Using try, except, else and finally blocks in conjuction
try:
    print(1 // 0)
except:
    print("Zero Division Error, You cannot divide by zero")
else:
    print("Exception has not occured")
finally:
    print("The finally block has been executed")