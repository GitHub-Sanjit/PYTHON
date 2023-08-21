class GrumpyDict(dict):
    def __repr__(self) -> str:
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    def __missing__(self,key):
        print(f"YOU WANT {key}? well in ain't here")
        
    def __setitem__(self,key,value):
        print(f"You want to change dictionary")
        print(f"Ok Fine")
        super().__setitem__(key,value)
        
    def __contains__(self,item):
        print("NO it ain't in here")
        return False
    
    
    
# MRO Genetics Solution
# Notice the order that Child inherits: Mother first and then Father.



class Mother:
    def __init__(self):
        self.eye_color = "brown"
        self.hair_color = "dark brown"
        self.hair_type = "curly"


class Father:
    def __init__(self):
        self.eye_color = "blue"
        self.hair_color = "blond"
        self.hair_type = "straight"


class Child(Mother, Father):
    pass