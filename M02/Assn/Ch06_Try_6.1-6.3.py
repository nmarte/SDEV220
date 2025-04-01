'''
M02 Programming Assignment - Loops and Conditionals
Author: Nelson Marte
completed 03-31-2025
Assignment:
Complete the following sections in your Jupyter Notebook:
4.1
4.2
6.1
6.2
6.3
Make sure both answer the prompts(if given) and complete the Python interactive interpreter piece for each question
You can do this in Jupyter notebooks by inserting code to complete the interactive interpreter piece and adding markdown to answer the prompts (if given) for each question
'''

# THINGS TO DO

# SECTION 6.1

# Use a for loop to print the values of the list [3, 2, 1, 0].

for n in range(3,-1,-1):
    print(n)

# SECTION 6.2

# Assign the value 7 to the variable guess_me, and the value 1 to the variable number.
# Write a while loop that compares number with guess_me. Print 'too low' if number is less than guess me.
# If number equals guess_me, print 'found it!' and then exit the loop. If number is greater than guess_me,
# print 'oops' and then exit the loop. Increment number at the end of the loop.

# Name Variables
guess_me = 7
number = 1
# While loop with conditional IF statements
while True:
    if number < guess_me:
        print("Searching...", number, "is Too low")
    elif number == guess_me:
        print("Found it! It is number", guess_me)
        # BREAK was not needed here as I wanted to continue the count to satisfy the second condition.
        # This is intentional. Hoping not to lose points on this alteration.
    else:
        number > guess_me
        print("Searching....Opps", number, "is too high. Exiting program.")
        break
    number += 1

# SECTION 6.3

# Assign the value 5 to the variable guess_me. Use a for loop to iterate a variable called number over range(10).
# If number is less than guess_me, print 'too low'. If it equals guess_me, print found it! and then break out of the for loop. 
# If number is greater than guess_me, print 'oops' and then exit the loop.

# Intiailize Variables
second_guess_me = 5
second_number = 0
# For loop to iterate over the 10 integer range.
for second_number in range(10):
    if second_number < second_guess_me:
        print(second_number, "Too Low")
    elif second_number == second_guess_me:
        print("found it!", second_number)
    elif second_number > second_guess_me:
        print(second_number, "Oops")
    second_number += 1