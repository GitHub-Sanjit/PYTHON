# import random

# random_number = random.randint(1,10)  # numbers 1 - 10
# guess = None

# while guess != random_number:
#     guess = int(input("Pick a number from 1 to 10: "))
#     if guess < random_number:
#         print("TOO LOW")
#     elif guess > random_number:
#         print("TOO HIGH!")
#     else:
#         print("YOU WON!!!!")   
# print(random_number)




import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("TOO LOW")
    elif guess > random_number:
        print("TOO HIGH!")
    else:
        print("YOU WON!!!!") 
        play_again = input("Do you want to play again? (y/n) ")  
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing")
            break




# handle user guesses
#   if they guess correct, tell them they won
#      otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!