from random import choice

places = ["McDonald's", "KFC", "Burger King", "Taco Bell"
    "Wendys", "Arby's", "Pizza Hut"]

def pick():
    """Return random fast food place"""
    return choice(places)