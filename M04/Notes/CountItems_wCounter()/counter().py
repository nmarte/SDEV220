# Speaking of counters, the standard library has one that does the work of the previous example 
# and more:
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

# The most_common() function returns all elements in descending order, 
# or just the top count elements if given a count:
breakfast_counter.most_common()
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

# You can combine counters. First, let’s see again what’s in breakfast_counter:
breakfast_counter
Counter({'spam':3, 'eggs':1})

# , we make a new list called lunch, and a counter called lunch_counter:
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)

# The first way we combine the two counters is by addition, using +:
print(breakfast_counter + lunch_counter)

# As you might expect, you subtract one counter from another by using -. 
# What’s for breakfast but not for lunch?
print(breakfast_counter - lunch_counter)

# Okay, now what can we have for lunch that we can’t have for breakfast?
print(lunch_counter - breakfast_counter)

# Similar to sets in Chapter 8, you can get common items by using the intersection operator &:
print(breakfast_counter & lunch_counter)

#The intersection chose the common element ('eggs') with the lower count. 
# This makes sense: breakfast offered only one egg, so that’s the common count.
# Finally, you can get all items by using the union operator |:
print(breakfast_counter | lunch_counter) # The item 'eggs' was again common to both. Unlike addition, union didn’t add their counts, but selected the one with the larger count.