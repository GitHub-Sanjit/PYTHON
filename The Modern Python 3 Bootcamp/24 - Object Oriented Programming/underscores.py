class Person:
    def __init__(self) -> None:
        self.name = "TONY"
        self._secret = "hi!"
        self.__msg = "I like turtles"
        self.__lol = "HAHAHAHAHAHAH"
        
p = Person()

print(p.name)
print(p._secret)
print(p._Person__msg)
print(p._Person__lol)