# This is an exercise on "Conditional Statements"

# if condition
x = int(raw_input("> Enter a number between '1' to '5'"))
if x == 1:
    print("This is an if bloack and you entered 1")
elif x > 2 and x < 5:
    print("This is an elifsw block and you entered a number between 2 and 5")
elif x>5:
    print("No Luck, you entered a number beyond the range")
else:
    print("This is the else block and you entered 5")

print("-------------------------------------------------------------------------")

# Applying the conditional statements to lists
data = list(range(1, 11))
y = int(raw_input("> Enter a number "))
if y in data:
    print("Entered number exists in the pre-determined data")
elif y not in data:
    print("Entered number does not exist in the pre-determined data")

print("-------------------------------------------------------------------------")