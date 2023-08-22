def fib_list(max):
    nums = []
    a,b = 0,1
    while len(nums) < max:
        nums.append(b)
        a,b = b, a+b
    return nums

def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x,y = y,x+y
        yield x
        count += 1

for n in fib_list(1000000):
    print(n)
    
    
    
    # Get Multiples Generator Solution


def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num
        
        
        
# Get Unlimited Multiples Solution
# This is similar to previous exercise, except it's simpler! We just loop forever (while True) instead of checking to see how many times we've looped.

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num
