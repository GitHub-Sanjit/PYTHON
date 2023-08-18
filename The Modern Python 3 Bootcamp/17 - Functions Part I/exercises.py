# Define a function product that returns the product of two numbers:

def product(a,b):
    return a*b

# ........................
# Here's a solution that uses what we've learned so far.

# Keep track of the days in a list.
# Check to make sure num isn't < 0 or> 6.
# Return the corresponding day. Use days[num-1] because return_day(1) should return 0th item in list.
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None
# BONUSADVANCEDVERSION:

# Here's a more advanced solution that involves error handling, which we have not covered yet. It eliminates the need to check to see if num is a valid indexin the list. We cover this in the debugging section, but I thought you may want to see if now.

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
    # ..................................
    
# First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

def last_element(l):
    if l:
        return l[-1]
    return None
# ...................
def number_compare(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
# ................................
# In my solution, I use the built-in count()  to count the number of times letter  appears in string .  I also downcase both string  and letter  to make it case-insensitive (you could also upcase both instead)

def single_letter_count(string,letter):
    return string.lower().count(letter.lower())
# .........................

# I used a dictionary comprehension. For each letter in the input string, I make the key the letter itself ("a" for example), and the corresponding value is the result of running count() of that letter in the string.

def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

# It's basically just a large if-elif-else statement:

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
# ........................
# Here's the simpler version that doesn't ignore whitespace. I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.

def is_palindrome(string):
    return string == string[::-1]
# The Bonus Version:
# For the more advanced version that ignores whitespace, Ifirst remove all whitespace from the input string using a string method calledreplace().What I'm actually doing is replacing all spaces(" ") with empty strings (""). Isave the result to a new variable I call stripped. Then, I simply check if strippedis a palindrome, using the same logic I did in the previous solution.

def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]
# ..................................

# Using the built-in count() method, this is really nice and easy:

def frequency(collection, searchTerm):
    return collection.count(searchTerm)
# ..............................
# In my solution, I start with a variable called total.
# Since we're working with multiplication, I start it off as 1.  
# Then I iterate through the list, checking if each num is cleanly divisible by 2
# If it is, I multiply total by the number
# At the end, after the loop finishes, I return total
def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total
# .......................
# My solution works by:

# Slicing the first character (up to index 1) and capitalizing it
# Adding that to the rest of the string (from index 1 onward)
def capitalize(string):
    return string[:1].upper() + string[1:]
# ....................
# With a list comprehension
# You can write compact  in a nice single line of code.  How compact!

def compact(l):
    return [val for val in l if val]
# Without a list comprehension
# I make a list to store all truthy values
# I iterate over each value in the list
# I check if the value is truthy (using a simple if val )
# If the value is truthy, add it to the truthy_vals  list
# return truthy_vals  at the end
def compact(l):
    truthy_vals = []
    for val in l:
        if val: truthy_vals.append(val)
    return truthy_vals
# ................
# Manual Looping Solution
# Here's one potential solution:

# Define an empty list that will eventually store the in common values
# Loop through one list (l1)
# For each value, check if that value is in the other list (l2)
# If it is, append the value to the in_common list
# Return in_common  after the loop ends
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common
# List Comprehension Solution
# The first solution is perfectly valid.  It's a more "traditional" way of solving the problem.  A more Python-ic solution involves using a list comprehension to do the same thing on a single line. Both work just as well.  It's a matter of personal preference, so don't get too caught up in it!



def intersection(l1, l2):
    return [val for val in l1 if val in l2]


# Sets Solution
# This solution(submitted by Sebastian on the discussion boards) is the most efficient of the three.  It converts the lists to sets, which removes duplicate values, and then finds the intersection of them using &.  If you need review, watch the sets section again (it's super short).



def intersection(list1, list2):
    return [val for val in set(list1) & set(list2)]

# .....................

# "Traditional" Version
# Here's my solution that doesn't use a list comprehension:

# I have two lists, to hold the true and false values
# I loop through the list, calling fn  with each value in the list
# If the result is True, I append the value to the trues  list
# Otherwise, I append the value to the falses  list
# At the end I return a list that contains both the trues  and falses  lists
def partition(lst, fn):
    trues = []
    falses = []
    for val in lst:
        if fn(val):
            trues.append(val)
        else:
            falses.append(val)
    return [trues, falses]


# List Comprehension Version
# Using a list comprehension, you can get this function down to a single line.  It's definitely a tradeoff though.  It's much short but also more difficult to understand.  It's a fine balance between brevity and readability. 

def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


# Another Solution
# This solution was submitted by a student named Jonathan.  Thanks, Jonathan!

def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)],l]
