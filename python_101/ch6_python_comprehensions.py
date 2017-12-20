# This is an exercise on "Python Comprehensions"

# List Comprehensions
x = [i for i in range(5)]
print(x)

y = list(range(1,11,1))

if [i for i in y if i>1]:
    print(i)

data = [i for i in range(10) if i % 2 == 0]
print(data)

names = ["Srinivas ", "Samuel", " Shankar "]
print([i.strip() for i in names])

print({i: str(i) for i in range(10)})

numbers = [1,2,3,4,5,2,3,4,5,6,7,7,8,9]
print(set(numbers))