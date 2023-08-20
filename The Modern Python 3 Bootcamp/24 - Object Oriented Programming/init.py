class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        
user1 = User("Joe","Smith",68)
user1 = User("Blanca","Lopez",41)


# Social Media Comment Class Solution:
# Here's my class definition for the Comment class.  Notice the default value for likes in the __init__() definition.



class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes