# This is an exercise on "Calculating BMR"

weight = 0
fat_percentage = 0
height = 0
age = 0
type = 'else'

def main():
    global weight
    global fat_percentage
    global height
    global age
    global type
    print("Welcome to the BMR calculator.\nPlease enter the below requested information one after the other")
    print("Enter your weight in Kg")
    weight = raw_input()
    print("Enter your fat percentage in percentage")
    fat_percentage = raw_input()
    print("Enter your Height in cm")
    height = raw_input()
    print("Enter your Age in years")
    age = raw_input()
    print("How would you like to calculate the BMR, enter 'squats' or 'regular'")
    type = raw_input()

#BMR = 66 + (13.7 x weight in kg) + (5 x height in cm) - (6.8 x age in years)
def bmr_regular(w,f,h,a):
    lean_mass = float(w) * (1-(float(f)/100))
    print("So, your weight is %s Kg, lean mass is %s Kg, height is %s cm and age is %s years"%(w, lean_mass, h, a))
    value = 66 + (13.7 * lean_mass) + (5 * float(h)) - (6.8 * float(a))
    return value

# SQUATS Formula = (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) + 5
def bmr_squats(w,f,h,a):
    lean_mass = float(w) * (1-(float(f)/100))
    print("So, your weight is %s Kg, lean mass is %s Kg, height is %s cm and age is %s years"%(w, lean_mass, h, a))
    value = (10 * lean_mass) + (6.25 * float(h)) - (5 * float(a)) + 5
    return value

main()

if type == 'squats':
    print("Great, your bmr is %d" %bmr_squats(weight, fat_percentage, height, age))
elif type == 'regular':
    print("Great, your bmr is %d" %bmr_regular(weight, fat_percentage, height, age))
else:
    print("Enter something")
    main()
