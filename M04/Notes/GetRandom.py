from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))

print(choice(('a', 'one', 'and-a', 'two')))

print(choice(range(100)))

print(choice('alphabet'))

# Use the sample() function to get more than one value at a time:
from random import sample
print((sample([23, 9, 46, 'bacon', 0x123abc], 3)))

print((sample(('a', 'one', 'and-a', 'two'), 2)))

print((sample(range(100), 4)))

print((sample('alphabet', 7)))

# To get a random integer from any range, you can use choice() or sample() with range(),
#  or use randint() or randrange():

from random import randint
print(randint(38,74))

print(randint(38,74))

print(randint(38,74))

# Finally, get a random real number (a float) between 0.0 and 1.0:
from random import random
print(random())