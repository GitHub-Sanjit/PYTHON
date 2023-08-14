# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is Unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is Even") 
#     else:
#         print(f"{num} is Odd")

    
for num in range(1,21):
    if num == 4 or num == 13:
        state = "Unlucky"
    elif num % 2 == 0:
        state = "Even"
    else:
        state = "Odd"
    print(f"{num} is {state}")