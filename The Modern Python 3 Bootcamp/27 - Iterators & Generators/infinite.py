# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     result = []
#     while len(result) < max:
#         if i >= len(nums): i = 0
#             result.append(nums[i])
#             i += 1
#         return result

# print(current_beat())

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1
        
        
# Make Song Generator Solution
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)