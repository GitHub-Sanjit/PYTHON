from random import choice
#  We can return function from other function
def make_laugh_func():
    def get_laugh():
        l = choice(("HAHAHAHAHAH ","lol", "tehhehe"))
        return l
    return get_laugh

laugh = make_laugh_func()
print(laugh())