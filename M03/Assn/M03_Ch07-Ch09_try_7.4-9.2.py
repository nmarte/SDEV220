'''
M02 Programming Assignment - Loops and Conditionals
Author: Nelson Marte
completed 04-07-2025
Assignment:
Complete the following sections in your Jupyter Notebook:
In your text book, navigate to the end of Chapter 7 to the section titled "Things to Do"
Complete the following sections in your Jupyter Notebook:
7.4
7.5
7.6
7.7
9.1
9.2
'''

# THINGS TO DO

# 7.4 Make a list called things with these three strings as elements: 
# "mozzarella", "cinderella", "salmonella".

things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# 7.5 Capitalize the element in things that refers to a person and then print the list. 
# Did it change the element in the list?

#things = [thing.capitalize() for thing in things]
things[1] = things[1].title()
print(things)

# 7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = things[0].upper()
print(things)

# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[-1]
print(things)

# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
names = ['Harry', 'Ron', 'Hermione']

def good(text):
    return text

print(good(names))

# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10).
# Use a for loop to find and print the third value returned.

# for i in range(10):
#    if i % 2 != 0:
#        print(i)

def get_odds(n):
    if n % 2 != 0:
        print(n)
