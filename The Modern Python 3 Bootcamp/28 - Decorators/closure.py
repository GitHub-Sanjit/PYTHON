from random import choice
#  Inner functions can access outer function scope
def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(("HAHAHAHAHAH ","lol", "tehhehe"))
        return f"{laugh} {person}"
    return get_laugh

laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())