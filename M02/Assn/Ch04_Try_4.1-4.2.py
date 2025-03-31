'''
M02 Programming Assignment - Loops and Conditionals
Author: Nelson Marte
completed 03-25-2025
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

# Section 4.1
# Choose a number between 1 and 10 and assign it to the variable secret. 
# Then, select another number between 1 and 10 and assign it to the 
# variable guess. Next, write the conditional tests (if, else, and elif) 
# to print the string 'too low' if guess is less than secret, 
# 'too high' if greater than secret, and 'just right' if equal to secret.

# Name Variables
secret = 7
guess = int(input("Please enter a wholenumber between 1 and 10: "))
if guess < 1 or guess > 10:
    print("Did you follow instructions?")
elif guess < secret:
    print("Too low a guess")
elif guess > secret:
    print("Too high a guess")
elif guess == secret:
    print("That's just right")
else:
    print("That's not a number.")


# Section 4.2
# Assign True or False to the variables small and green. 
# Write some if/else statements to print which of these matches 
# those choices: cherry, pea, watermelon, pumpkin.

small = True
green = True
if small:
    if green:
        print("That is most likely a pea")
    else:
        print("That's probably cherry")
else:
    if green:
        print("It's a watermelon")
    else:
        print("It's probably a pumpkin")

