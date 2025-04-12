from random import choice
print(choice([23, 9, 46, 'bacon', 0x123abc]))

print(choice(('a', 'one', 'and-a', 'two')))

print(choice(range(100)))

print(choice('alphabet'))

# Use the sample() function to get more than one value at a time:
from random import sample
