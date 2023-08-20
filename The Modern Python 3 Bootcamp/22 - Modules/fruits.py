# import bananas
# import termcolor
from bananas import dip_in_chocolate as dip
import apples

print(dip())
print(apples.offer())


# Custom Module Exercise
# This exercise tested your ability to write simple code in one file and import it into another file.

# In helpers.py:
# I started by defining lucky_number in helpers.py:

def lucky_number():
  return 37
# In exercise.py:
# import my helpers module first. And then I call helpers.lucky_number() and save the result to the num variable

#Import your helpers module here. Do not use the 'from' or 'as' syntax, just use a plain old 'import'
# import helpers


#Call the lucky_number function from your helpers module, and save the result to a variable called num
# num = helpers.lucky_number()



# * If you are using Mac or Linux, you can ignore this lecture note.

# In the video lecture that follows, we install and use an external module called termcolor which does not work on Windows Powershell by default.

# To make the ANSI colors used in termcolor work within Windows Powershell, you will also need to import/init the colorama module - https://pypi.python.org/pypi/colorama

# We will cover how to install the termcolor module via pip in the video lecture that follows. Make sure to also install the colorama module using the same approach (via pip) while following the upcoming video lecture.

# Then, try using this code:

# from colorama import init
# from termcolor import colored
 
# # use colorama to make termcolor work on Windows too
# init()
 
# # then use termcolor for all colored text output
# print(colored('Hello, World!', 'green', 'on_red'))
# After using this approach, you should also be seeing a colored text output in Windows Powershell!