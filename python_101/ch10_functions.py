# This is an exercise on "Functions"

# empty function or a stub
def a_function():
    pass

# function with arguments
def add(a,b):
    print(a+b)

add(2,3)

print("-------------------------------------------------")

# function with a return value
def product(a,b):
    value = a*b;
    return value

print(product(3,4))

print("-------------------------------------------------")

def substract(a=3, b=1):
    return a-b

print(substract())
print("-------------------------------------------------")
print(substract(4,1))
print("-------------------------------------------------")
print(substract(b = 8, a = 2))
print("-------------------------------------------------")

# ars functions
def addition(*args):
    value = 0
    for a in args:
        value += a
    return value

print addition(2,3,4)
print("-------------------------------------------------")

# focus on the *kwargs functions