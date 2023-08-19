def square(num): return num * num

square2 = lambda num: num * num

add = lambda a,b: a + b

# print(square2(7))
# print(add(3,10))

print(square.__name__)
print(square2.__name__)
print(add.__name__)


# It's a super short solution! This lambda takes a parameter and returns the cube of that number.  The lambda itself is saved in the cube  variable.

cube = lambda num: num ** 3