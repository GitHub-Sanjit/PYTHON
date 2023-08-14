# while True:
#     command = input("Type 'exit' to exit: ")
#     if(command == "exit"):
#         break

# for x in range(1,101):
#     print(x)
#     if(x == 3):
#         break

times = input("How many times do I have to tell You? ")
times = int(times)

for time in range(times):
    print("CLEAN UP YOUR ROOM!")
    if time >= 3:
        print("Do you even listen anymore?")
        break



from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10) #update number to be a new random int from 1-10