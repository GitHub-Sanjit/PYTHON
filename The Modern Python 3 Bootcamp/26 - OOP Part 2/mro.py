class A:
    def do_something(self):
        print("Method Defined In: A")
        
class B(A):
    def do_something(self):
        print("Method Defined IN: B")
        super().do_something()
        
class C(A):
    def do_something(self):
        print("Method Defined In: C")
        
class D(B,C):
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()
    
 
# print(D.__mro__)       
# print(D.mro())       
# help(D)
# thing = D()
# thing.do_something()

thing = D()
thing.do_something()




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