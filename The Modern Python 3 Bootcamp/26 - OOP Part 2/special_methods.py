from copy import copy
class Human:
    def __init__(self, first, last, age) -> None:
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self) -> str:
        return f"Human named {self.first} {self.last}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        return "Can't Multiply"


j = Human("Jenny","Larsen",47)
k = Human("Kevin","Jones",49)

triplets = j*3
triplets[1].first = "Jessica"
print(triplets)