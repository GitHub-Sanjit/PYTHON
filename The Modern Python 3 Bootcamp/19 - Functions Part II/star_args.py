def ensure_correct_info(*args):
    # print(args)
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt"
    return "Not sure who you are"
print(ensure_correct_info("hello",False,78)) # Not sure who you are
print(ensure_correct_info(1,True,"Steele","Colt"))



# Here's my solution:
# Remember, I don't need to write the else  part of the conditional in this case, because I'm returning out of the function on the line before. So the only way the return False  line runs is if the above line didn't run.  It's an implicit else .

def contains_purple(*args):
    if "purple" in args: return True
    return False