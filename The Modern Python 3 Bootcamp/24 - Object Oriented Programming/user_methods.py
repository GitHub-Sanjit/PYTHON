class User:
    def __init__(self,first,last,age) -> None:
        self.first = first
        self.last = last
        self.age = age
        
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
        
user1 = User("Joe", "Smith",68)        
user2 = User("Blanca", "Lopez",41)        

# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)
# print(user2.full_name())
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user1.initials())
# print(user2.initials())

print(user1.is_senior())
print(user2.birthday())
print(user1.age)




# Bank Account Exercise Solution:
# Here's my BankAccount class:

class BankAccount:

    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

