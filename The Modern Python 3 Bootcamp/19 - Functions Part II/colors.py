def fav_colors(**kwargs):
	for person, color in kwargs.items():
		print(f"{person}'s favorite color is {color}")

fav_colors(colt="purple", ruby="red", ethel="teal")
fav_colors(colt="purple", ruby="red", ethel="teal", ted="blue")
fav_colors(colt="royal deep amazing purple")



# combine_words solution
# I check if kwargs contains "prefix".
# If it does, I return the value of prefix + the word
# Otherwise, I check to see if "suffix" was provided as a kwarg
# If it was, I return the word followed by the value of suffix
# Otherwise, I just return the word on its own.
def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word
