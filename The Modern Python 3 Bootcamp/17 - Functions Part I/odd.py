def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False
print(is_odd_number(5))


# Here's the initial broken state of the function:

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count
# The problem is that the function returns the very first time through the loop because of the way return is indented.

# To fix it, all we have to do is outdent the return statement so that it now only returns after the loop finishes running

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count