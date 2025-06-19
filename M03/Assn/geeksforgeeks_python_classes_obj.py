'''
Python Classes and Objects
https://www.geeksforgeeks.org/python-classes-and-objects/
'''

# define a class
#class Dog:
#    sound = "bark" # class attribute

# Create an object form the class
#dog1 = Dog()

# Access the class attribute
#print(dog1.sound)


''' Initiate Object with __init__ '''
class Dog:
    species = "Canine" # Class attribute

    def __init__(self, name, age):
        self.name = name # Instance attribute
        self.age = age # Instance attribute

# Creating an object of the Dog class
# The obj is a variable(instance) assigned to Class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Seven", 7)

print(dog1.name) # Output: Buddy
print(dog2.name)
print(dog1.species) # Output: Canine 
print(dog1.age)

''' Self Parameter '''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} is barking!')

# Creating an instance of Dog
dog1 = Dog("Buddy", 3)
dog1.bark()

'''
Explanation:

Inside bark(), self.name accesses the specific dog's name and prints it.
When we call dog1.bark(), Python automatically passes dog1 as self, allowing access to its attributes.
'''


''' __str__ Method '''
