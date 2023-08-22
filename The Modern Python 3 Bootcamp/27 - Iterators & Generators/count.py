def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))


# Week Generator Solution
# Define the generator function week  which has a list of days.  Iterate over the days and yield each day.   After "Sunday", the generator is exhausted.  It does not start over.



def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day
        
        
# Yes Or No Generator Solution
# yes_or_no  loops forever (while True) and yields answer , and then toggles answer from yes to no, or vice versa.

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"