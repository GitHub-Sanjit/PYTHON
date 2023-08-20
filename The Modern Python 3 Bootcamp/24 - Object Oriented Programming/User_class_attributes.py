class User:
    
    active_users = 0
    
    def __init__(self,first,last,age) -> None:
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self,thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
        
# user1 = User("Joe", "Smith",68)        
# user2 = User("Blanca", "Lopez",41)        

# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user2.full_name())
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user1.initials())
# print(user2.initials())

# print(user1.is_senior())
# print(user2.birthday())
# print(user1.age)

print(User.active_users)
user1 = User("Joe", "Smith",68)        
user2 = User("Blanca", "Lopez",41)  
print(User.active_users)
print(user2.logout())
print(User.active_users)