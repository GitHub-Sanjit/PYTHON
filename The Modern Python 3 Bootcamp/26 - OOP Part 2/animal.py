class Animal:
    def __init__(self,name, species) -> None:
        self.name = name
        self.species = species
    
    def __repr__(self) -> str:
        return f"{self.name} is a {self.species}"

    def make_sound(self,sound):
        print(f"this animal says {sound}")
        
        
class Cat(Animal):
    def __init__(self, name,breed,toy) -> None:
        super().__init__(name,species="Cat")
        self.breed = breed
        self.toy  = toy
        
    def play(self):
        print(f"{self.name} plays with {self.toy}")
    
    
    
       
blue = Cat("Blue","Scottish Fold","String")
blue.play()
# blue.make_sound("mewe")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

# print(isinstance(blue,object))