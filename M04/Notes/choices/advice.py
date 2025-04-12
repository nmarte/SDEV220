from random import choice

answers = ["Yes!", "No!", "Reply Hazy", "Sorry, what?"]

def give():
    """Return random advice"""
    return choice(answers)