# for num in range(10):
#     print(num)

for num in range(0,100,5):
    print(num)



# Solution Using a Conditional

# This solution loops over all the numbers between 10 and 20, checking to see if the number is even inside the loop.

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0


# YOUR CODE GOES HERE:
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n


# Solution using range step
# Instead of looping over every number between 10 and 20, this solution only loops over the oddnumbers. Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by. Thanks for sharing your version, Abdul.

x = 0

for i in range(11,21,2):
        x += i
