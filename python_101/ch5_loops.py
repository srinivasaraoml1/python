# This is an exercise on "Working with Loops"

# Loops are used when you want to do the same thing many times
# For loop
# range functions comes into play when the for loop has to be used, look at the demo below:
x = range(5)
# Here x is a list type with the size 5
print(x)

# Format of range function: range(start, end, interval)
# The range function includes the start varibale, but excluded the end variable and breaks the flow as per the inteval variable
# default start variable is taken as '0' and the default interval is taken as '1'
y = range(1, 10, 2)
print(list(y))

# Applying the range function to for loops
# for lists
for i in range(5):
    print(i)
# for dictionaries
my_dict = {"a": "1", "b": "2", "c": "3", "d": "4"}
print("----------------------------")
print("Unordered Key, Value pairs are:")
print("----------------------------")
for key in my_dict.keys():
    print("[Keys, Value] is : [%s, %s]"%(key,my_dict[key]))


# We can observe that keys are picked in a random order as the dictionaries are unorder, we can avoid this issue with sorted function fo rlists
print("----------------------------")
print("Sorted Key, Value pairs are:")
print("----------------------------")
for key in sorted(my_dict.keys()):
    print("[Keys, Value] is : [%s, %s]"%(key,my_dict[key]))

print("----------------------------")

# Using loops with range and prining only the even numbers
for x in range(10):
    if x % 2 == 0:
        print(x)

print("----------------------------")

# While Loops:
i = 0
while i < 10:
    print(i)
    i += 1

print("----------------------------")

# while with a conditional check to break the loop
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

print("----------------------------")

# while with conditions
j=0
while i<10:
    if j == 3 or j == 5:
        j += 1
        continue
    print(j)
    if j == 7:
        break
    j += 1

print("----------------------------")

# For loop with a condition
my_list=[1,2,3,4,5]
for i in my_list:
    if i == 3:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")