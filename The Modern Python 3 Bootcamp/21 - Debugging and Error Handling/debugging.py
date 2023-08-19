# import pdb
# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)


def add_numbers(a,b,c,d):
    import pdb; pdb.set_trace()
    
    return a+b+c+d

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)


# Division Exercise Solution
# Here's my version of the divide function:

def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total