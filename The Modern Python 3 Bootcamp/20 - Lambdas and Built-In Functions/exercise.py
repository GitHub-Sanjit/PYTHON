# Interleaving Strings Solution
# Here's a detailed walkthrough. Iknow it can be overwhelming, but try to step through one piece at a time if you get stuck.

# I start by defining interleave, which accepts 2 strings: str1, and str2

# To make this easier, let's use an example. Let's say that I callinterleave('hi', 'no')

# Focus on the innermost bit first. I zip the two strings together, which returns a list of tuples like: [('h','n'), ('i','o')]

# To get it back into a string, Ineed to:

# First join the individual tuples into strings, which is what the first join()does

# it results in a list of strings:['hn', 'io']

# Finally, join all the remaining strings into one large string

# results in'hnio'

# Return the result!

def interleave(str1,str2):
  return ''.join(''.join(x) for x in (zip(str1,str2)))



# Triple and Filter Solution
# For my solution, I chose to use map and filter in combination.

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))



# Extract Full Name Solution
# I use map and a lambda to create a new list full of formatted strings:



def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
