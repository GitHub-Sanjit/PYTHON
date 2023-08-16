# colors = ["purple", "teal", "magenta"]

# for color in colors:
#     print(color)


# numbers = [4,6,2,9,7,10]
# for num in numbers:
#     print(num*num)


# numbers = [1,2,3,4]
# i = 0
# while i< len(numbers):
#     print(numbers[i] * 3)
#     i+=1


colors = ["purple", "teal", "magenta","crimson","emerald"]

index = 0
while index < len(colors):
    print(f"{index + 1}: {colors[index]}")
    index += 1
    
    
    
# Here are two potential solutions.  You can either capitalize each string as you add it to result:

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()


# Or, you can add all strings to result, and then capitalize the whole thing once at the end.

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()


# A solution using append()

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"

instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
# A solution using extend()

# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])



# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list
instructors.pop()

# Remove the first value in the list
instructors.pop(0)

# Add the string "Done" to the beginning of the list
instructors.insert(0, 'Done')
