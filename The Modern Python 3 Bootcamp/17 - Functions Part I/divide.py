def divide(num1,num2):
    return num1/num2
print(divide(2,5))
print(divide(5,2))


# Using string concatenation:

def yell(word):
    return word.upper() + "!"
# Using the string format() method:

def yell(word):
    return "{}!".format(word.upper())
# Using an f-string. My personal favorite, but only works in python 3.6 or later.  Udemy exercises don't support it currently :(

def yell(word):
    return f"{word.upper()}!"