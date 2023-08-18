cities = ['Los Angeles','Los Angeles','Los Angeles', 'Florence', 'Florence', 'Florence', 'Boulder', 'Oslo','Oslo','Oslo','Tokyo','Santiago','Kyoto', 'San Francisco','Shanghai']

print(list(set(cities)))


# Suppose I teach two classes:
math_students = {"Matthew", "helen","Prashant","James","Aparna"}
biology_students = {"Jane","Matthew","Charlotte","Mesut","Oliver","James"}

# To generate a set with all my unique students
math_students | biology_students

# To generate a set with students who are in both courses
math_students & biology_students



# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)

# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)

# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)