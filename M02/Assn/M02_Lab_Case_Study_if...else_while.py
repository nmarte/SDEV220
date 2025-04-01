'''
Module 2 Lab - Case Study: if...else and while
Author: Nelson Marte
completed 03-31-2025
Assignment:
Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
ask for and accept a student's last name.
quit processing student records if the last name entered is 'ZZZ'.
ask for and accept a student's first name.
ask for and accept the student's GPA as a float.
test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
Test your app using at least five students.
Your header comments need to contain
Your name
The file name for your app
A brief description of what your app will do
'''
# Initialize Variables

while True:
    l_name = input("Please enter the student's last name [or enter 'zzz' to quit]: ")
    if l_name == 'zzz':
        break
    gpa = float(input("Please enter the GPA: "))
    if gpa >= 3.5:
        print(l_name.title(), "has made the Dean's List!")
    elif gpa >= 3.25:
        print(l_name.title(), "has made a Honor Roll!")
    elif gpa >= 0 and gpa < 3.25:
        print(l_name.title(), "has a good grade.")
