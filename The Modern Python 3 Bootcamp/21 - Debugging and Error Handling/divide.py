def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("dont divide by zero please!...")
    except TypeError:
        print("a and must be int or floats")
    else:
        print(f"{a} divided by {b} is {result}")
        
print(divide(1,2))
print(divide(1,0))