# This is an exercise on "Lists, Tuples and Dictionaries"

# Lists : Research more on List slicing
# Setting up an empty or dummy list
data = []
names = list()

# Lists with data
numbers = [1,2,3,4,5,6]
print(numbers)
dnames = ["Srinivas", "Baskar", "Sangameswari", "Shyamala", "Sowmya", "Praveena"]
print(dnames)
# Nested Lists
data1 = [numbers, dnames]
print(data1)

# list functions
print(names + dnames)

dnames.sort()
print(dnames)

# Tuples
my_tuple=(1,2,3,4,5)
print(my_tuple[0:3])
another_tuple = tuple()
abc = tuple([1, 2, 3])
print(abc)
print(list(abc))

# Dictionaries : These are basically a Hash Map[Key, Value Pairs]
dict = {}
print(dict)
dict1 = dict
print(dict1)
dict2 = {'a':'1', 'b':'2', 'c':'3'}
print(dict2)

print('a' in  dict2)

print(dict2.keys())