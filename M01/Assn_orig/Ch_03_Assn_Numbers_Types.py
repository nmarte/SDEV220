'''
M01 Programming Assignment - Numbers and Types
Author: Nelson Marte
completed 10-12-2024
Assignment:
Complete sections 3.1 through 3.6 utilizing your Jupyter Notebook
Make sure both answer the prompts(if given) and complete the Python interactive interpreter piece for each question
You can do this in Jupyter notebooks by inserting code to complete the interactive interpreter piece and adding markdown to answer the prompts (if given) for each question
'''

# THINGS TO DO

# Section 3.1 How many seconds are in an hour? Use the interactive interpreter as a calculator 
# and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60).

# Name the variables
seconds = 1
minute = seconds*60
hour = minute*60

print("The total seconds in one hour are", hour)

# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

seconds_per_hour = hour

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.
# Multiply the variable 'seconds_per_hour' by # of hours in a day int(24)

print("There are", seconds_per_hour*24,"seconds in one day")

# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day
seconds_per_day = seconds_per_hour*24