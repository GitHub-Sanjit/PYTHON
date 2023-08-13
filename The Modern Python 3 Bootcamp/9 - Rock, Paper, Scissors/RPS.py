# p1 = input("Player 1: rock, paper, or scissors ")
# p2 = input("Player 2: rock, paper, or scissors ")
 
# if p1 == p2:
#     print("Draw")
# elif p1 == "rock" and p2 == "scissors":
#     print("p1 wins")
# elif p1 == "paper" and p2 == "rock":
#     print("p1 wins")
# elif p1 == "scissors" and p2 == "paper":
#     print("p1 wins")
# else:
#     print("p2 wins")

from random import randint

player = input("Player 1, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'rock'
else:
    computer = 'scissors'

print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    else:
        print("computer wins!")
else:
    print("Something went wrong")
