def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper
@be_polite
def greet():
    print("My name is colt.")

@be_polite    
def rage():
    print("I hate You")
    
# we are decorating our function
# with politeness!
# greet = be_polite(greet)
# r = be_polite(rage)
# r()
# greet()
# greet()
# greet()
# greet()
rage()