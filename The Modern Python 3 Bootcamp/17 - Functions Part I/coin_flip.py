from random import random

# def flip_coin():
#     # generate a random number 0-1
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
    
# print(flip_coin())


def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"
    
print(flip_coin())


def speak_pig():
    return 'oink'


# Generating evens using a list comprehension:

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]
# Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result

