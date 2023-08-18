def add(a,b):
    return a+b

def math(a,b,fn=add):
    return fn(a,b)

def subtract(a,b):
    return a-b

print(math(2,2))

print(math(2,2,subtract))



# The most straightforward solution is to use a large if-elif-else statement:

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
         return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    else:
        return "?"
# Another shortersolution involves using adictionary that maps animal names to noises.

noises = {
    "dog": "woof", 
    "pig": "oink", 
    "duck": "quack", 
    "cat": "meow"
}
# Then, we just use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise.get() will returnNone if the animal is not in the dictionary. Then we just check to see if noise exists. If it does, return noise. Otherwise, return "?"

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
# Thanks to Todd for sharing his even more compact solution which passes in a default value to get()





def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')