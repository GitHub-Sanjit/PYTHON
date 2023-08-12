city = input('Where do you live?')

if city == 'los angeles' or city == 'San Francisco':
    print('You live in California')
else:
    print("You live in somewhere else")


# NO TOUCHING ======================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])
# NO TOUCHING ======================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if food == 'apple' or food == 'grape':
    print ("fruit")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("yuck")
