playlist = {
    'title':'patagonia bus',
    'author':'colt steele',
    'songs':[
        {'title': 'song1','artist':['blue'], 'duration':2.5},
        {'title': 'song2','artist':['kitty','djcat'], 'duration':5.25},
        {'title': 'meowmeow','artist':['garfield'], 'duration':2.0},
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)



# Using a dictionary comprehension:

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0,3)}

# The "advanced" solution. We'll cover zip()  later on in the course.





list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

dict(zip(list1,list2))  



# There are many potential solutions for this:

# Using a dictionary comprehension 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}
# An alternate solution using a dict comprehension, without any references to list indexes:

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}
# Finally, a really simple solution.  If you have a list of pairs, you can very easily turn it into a dictionary using dict() 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)



# Using a dictionary comprehension:

answer = {char:0 for char in 'aeiou'} 

# Using dict.fromkeys:

# 
answer = dict.fromkeys("aeiou", 0) 


# Use chr() on the numbers between 65 and 91:

answer = {count: chr(count) for count in range(65,91)} 